package com.example.estsharabot.ui.fragments

import android.os.Bundle
import android.util.Log
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.Toast
import androidx.fragment.app.Fragment
import androidx.lifecycle.ViewModelProvider
import androidx.navigation.findNavController
import com.example.estsharabot.R
import com.example.estsharabot.databinding.FragmentMedicalHistoryBinding
import com.example.estsharabot.model.UserMedicalHistory
import com.example.estsharabot.repo.RemoteRepo
import com.example.estsharabot.viewmodel.RegisterViewModel
import com.example.estsharabot.viewmodel.RegisterViewModelFactory
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.GlobalScope
import kotlinx.coroutines.launch


class MedicalHistoryFragment : Fragment() {


    private val TAG = "MedicalHistoryFragment"
    private var _binding: FragmentMedicalHistoryBinding? = null
    private val binding get() = _binding!!

    private lateinit var viewModel: RegisterViewModel

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)

    }

    override fun onCreateView(
        inflater: LayoutInflater, container: ViewGroup?,
        savedInstanceState: Bundle?
    ): View? {
        // Inflate the layout for this fragment
        _binding = FragmentMedicalHistoryBinding.inflate(inflater, container, false)
        val view = binding.root

        binding.progressBar.visibility = View.GONE

        binding.btnRegister.setOnClickListener {
            binding.progressBar.visibility = View.VISIBLE

            val _1 = binding.inAnswer1.text?.toString()
            val _2 = binding.inAnswer2.text?.toString()
            val _3 = binding.inAnswer3.text?.toString()
            val _4 = binding.inAnswer4.text?.toString()
            val _5 = binding.inAnswer5.text?.toString()
            val _6 = binding.inAnswer6.text?.toString()
            val _7 = binding.inAnswer7.text?.toString()
            val _8 = binding.inAnswer8.text?.toString()

            try {
                val newReport = UserMedicalHistory(_1!!, _2!!, _3!!, _4!!, _5!!, _6!!, _7!!, _8!!)
                viewModel = ViewModelProvider(
                    this,
                    RegisterViewModelFactory(RemoteRepo())
                )[RegisterViewModel::class.java]
                GlobalScope.launch(Dispatchers.IO) {
                    val res = viewModel.registerMedicalHistory(newReport)
                }
                binding.progressBar.visibility = View.GONE
                Toast.makeText(activity, "Successfully Registered", Toast.LENGTH_SHORT).show()
                view.findNavController()
                    .navigate(R.id.action_medicalHistoryFragment_to_loginFragment)
            }catch (e :Exception){
                Log.e(TAG , "Error :${e.message}")
            }



        }


        return view

    }


}