@file:OptIn(DelicateCoroutinesApi::class)

package com.example.estsharabot.ui.fragments

import android.app.Activity
import android.content.Context
import android.content.Intent
import android.net.Uri
import android.os.Bundle
import android.provider.MediaStore
import android.util.Log
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.Toast
import androidx.activity.OnBackPressedCallback
import androidx.fragment.app.Fragment
import androidx.fragment.app.FragmentActivity
import androidx.lifecycle.ViewModelProvider
import androidx.navigation.fragment.NavHostFragment.Companion.findNavController
import androidx.recyclerview.widget.LinearLayoutManager
import androidx.recyclerview.widget.RecyclerView
import com.example.estsharabot.R
import com.example.estsharabot.adapters.LiveChatAdapter
import com.example.estsharabot.databinding.FragmentChatBinding
import com.example.estsharabot.model.Message
import com.example.estsharabot.remote.Service
import com.example.estsharabot.repo.RemoteRepo
import com.example.estsharabot.utility.BackPressedDialog
import com.example.estsharabot.utility.Constants
import com.example.estsharabot.utility.URIPathHelper
import com.example.estsharabot.viewmodel.ChatViewModel
import com.example.estsharabot.viewmodel.ChatViewModelFactory
import com.google.firebase.ktx.Firebase
import com.google.firebase.remoteconfig.FirebaseRemoteConfig
import com.google.firebase.remoteconfig.ktx.remoteConfig
import com.google.firebase.remoteconfig.ktx.remoteConfigSettings
import kotlinx.coroutines.*
import okhttp3.MediaType.Companion.toMediaTypeOrNull
import okhttp3.MultipartBody
import okhttp3.RequestBody
import okhttp3.RequestBody.Companion.asRequestBody
import java.io.File


class ChatFragment : Fragment() {


    private val TAG = "CHAT_FRAGMENT"

    private var _binding: FragmentChatBinding? = null
    private val binding get() = _binding!!

    private lateinit var uri: Uri
    private val pickImage = 100

    private var mList = ArrayList<Message>()

    private lateinit var messagesAdapter: LiveChatAdapter
    private lateinit var messageRecyclerView: RecyclerView

    private lateinit var viewModel: ChatViewModel

    var errorFlag = false
    private var imgUploadFlag = false
    private var firstMessageFlag = true
    private var counter = 0

    private val callBack = object : OnBackPressedCallback(true) {
        override fun handleOnBackPressed() {
            BackPressedDialog().show(
                childFragmentManager, TAG
            )
            GlobalScope.launch(Dispatchers.Main) {
                handleBackPressed()
            }


        }
    }

    override fun onCreateView(
        inflater: LayoutInflater, container: ViewGroup?, savedInstanceState: Bundle?
    ): View {

        _binding = FragmentChatBinding.inflate(inflater, container, false)
        val view = binding.root

        Constants.BASE_URL = getAPI(requireActivity(), Constants.CHAT_KEY)

        requireActivity().onBackPressedDispatcher.addCallback(callBack)

        initConnection()

        binding.btnSend.setOnClickListener {
            if (!errorFlag) {
                if (binding.etMessage.text.isNotEmpty()) {
                    send(Message(binding.etMessage.text.toString(), true))
                }

            }
        }

        return view
    }

    private fun initRecyclerView() {
        try {
            val layoutManager = LinearLayoutManager(context)
            messagesAdapter = context?.let { LiveChatAdapter(it, mList) }!!
            messageRecyclerView = binding.rvMessages
            messageRecyclerView.adapter = messagesAdapter
            messageRecyclerView.layoutManager = layoutManager
            messageRecyclerView.smoothScrollToPosition(mList.size - 1)
        } catch (e: Exception) {
            Log.e(TAG, "Failed to get instance: ${e.message}")
        }

    }

    private fun initConnection() {
        try {
            Constants.BASE_URL = getAPI(requireActivity(), Constants.CHAT_KEY)
            viewModel = ViewModelProvider(
                this, ChatViewModelFactory(RemoteRepo(Service.getInstance()!!))
            )[ChatViewModel::class.java]

            GlobalScope.launch(Dispatchers.IO) {
                getResponse(Message("Hi", true))
            }
        } catch (e: Exception) {
            Log.e(TAG, "Failed to get instance: ${e.message}")
            Toast.makeText(context, "Connection Error", Toast.LENGTH_LONG).show()
        }
    }

    private fun send(message: Message) {

        GlobalScope.launch(Dispatchers.IO) {
            getResponse(message)
        }

        mList.add(message)

        binding.etMessage.text.clear()
        binding.etMessage.hint = "Type a message"
        initRecyclerView()
        messagesAdapter.notifyItemInserted(mList.size - 1)
        messageRecyclerView.smoothScrollToPosition(mList.size - 1)
    }


    private suspend fun getResponse(message: Message) {
        var bye = false
        val text = viewModel.postMessage(message).text
        Log.d(TAG, "response : $text")

        when (text) {
            "Failed" -> {
                mList.add(Message(getString(R.string.ChatBotError), false))
                errorFlag = true
                binding.etMessage.isFocusable = false
            }

            "Bye" -> {
                mList.add(Message(text, false))
                bye = true
            }
            getString(R.string.upload_flag) ->{
                mList.add(Message(text, false))
                imgUploadFlag = true


            }

            else -> {
                mList.add(Message(text, false))
                binding.etMessage.isFocusable = true
            }
        }
        withContext(Dispatchers.Main) {
            if(bye){
                binding.etMessage.isFocusable = false
                delay(1000)
                send(Message("/restart", true))
                BackPressedDialog.waitFlag = null
                findNavController(this@ChatFragment).navigate(R.id.action_chatFragment_to_homeFragment)
            }

            initRecyclerView()
            messagesAdapter.notifyItemInserted(mList.size - 1)
            messageRecyclerView.smoothScrollToPosition(mList.size - 1)
            if (imgUploadFlag){
                imgUploadFlag = false
                Constants.IMAGE_BASE_URL = getAPI(requireActivity(), Constants.IMAGE_UPLOAD_KEY)
                delay(1500)
                val gallery = Intent(Intent.ACTION_PICK, MediaStore.Images.Media.INTERNAL_CONTENT_URI)
                startActivityForResult(gallery, pickImage)
            }
        }

    }


    @Deprecated("Deprecated in Java")
    override fun onActivityResult(requestCode: Int, resultCode: Int, data: Intent?) {
        super.onActivityResult(requestCode, resultCode, data)
        if (resultCode == Activity.RESULT_OK && requestCode == pickImage) {
            uri = data?.data!!
            GlobalScope.launch(Dispatchers.Main) {
                Constants.IMAGE_BASE_URL = getAPI(requireActivity(), Constants.IMAGE_UPLOAD_KEY)
                Log.d(TAG, Constants.BASE_URL)
                uploadImage(uri, requireContext())
            }

        } else {
            Toast.makeText(context, "Task Failed", Toast.LENGTH_LONG).show()
        }
    }

    private suspend fun uploadImage(uri: Uri, context: Context) {
        //convert uri to file
        val path = URIPathHelper().getPath(requireActivity(), uri)
        Log.d("RepositoryPosting", "String from fragment" + path.toString())
        val imageFile = File(path!!)

        val imageRequestFile: RequestBody = imageFile.asRequestBody("image/*".toMediaTypeOrNull())

        val requestBody: RequestBody = MultipartBody.Builder().setType(MultipartBody.FORM)
            .addFormDataPart("Frame", "Frame", imageRequestFile).build()

        //val res = viewModel.postImage(requestBody, uri, context, this, viewLifecycleOwner)
        //Log.d(TAG, "URL " + res.imageURL)
        //Log.d(TAG, "URL " + res.organ)
        //Log.d(TAG, "URL " + res.percentage)
        //Log.d(TAG, "URL " + res.disease)
        //getResponse(Message("yes",true))

    }

    private suspend fun handleBackPressed() {
        if (BackPressedDialog.waitFlag.isNullOrEmpty()) {
            delay(500)
            handleBackPressed()
        } else if (BackPressedDialog.waitFlag == "Discard") {
            Log.d(TAG, "in if")
            send(Message("/restart", true))
            BackPressedDialog.waitFlag = null
            findNavController(this@ChatFragment).navigate(R.id.action_chatFragment_to_homeFragment)
        } else if (BackPressedDialog.waitFlag == "Stay") {
            BackPressedDialog.waitFlag = null
        }
    }


    private fun getAPI(activity: FragmentActivity, key: String): String {
        var url = ""
        val remoteConfig: FirebaseRemoteConfig = Firebase.remoteConfig
        val configSettings = remoteConfigSettings {
            minimumFetchIntervalInSeconds = 0
        }
        remoteConfig.setConfigSettingsAsync(configSettings)
        activity.let {
            remoteConfig.fetchAndActivate().addOnCompleteListener(it) { task ->
                if (task.isSuccessful) {
                    val updated = task.result
                    Log.d(TAG, "Config params updated: $updated")


                } else {
                    try {
                        Toast.makeText(
                            activity,
                            "Please check your internet connection",
                            Toast.LENGTH_SHORT
                        ).show()
                    } catch (e: Exception) {
                        Log.e(TAG, "Toast Problem : ${e.message}")
                    }

                }
            }
        }
        url = Firebase.remoteConfig.getString(key)
        Log.d(TAG, url)
        return if (url == "") {
            Constants.IMAGE_BASE_URL
        } else {
            url
        }
    }
}