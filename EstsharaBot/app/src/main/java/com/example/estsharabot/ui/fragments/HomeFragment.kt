package com.example.estsharabot.ui.fragments

import android.os.Bundle
import android.util.Log
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import androidx.fragment.app.Fragment
import androidx.navigation.findNavController
import com.example.estsharabot.R
import com.example.estsharabot.databinding.FragmentHomeBinding
import com.example.estsharabot.model.User
import com.example.estsharabot.utility.Constants
import com.google.firebase.database.DataSnapshot
import com.google.firebase.database.DatabaseError
import com.google.firebase.database.DatabaseReference
import com.google.firebase.database.ValueEventListener
import com.google.firebase.database.ktx.database
import com.google.firebase.ktx.Firebase


class HomeFragment : Fragment() {

    private var _binding: FragmentHomeBinding? = null
    private val binding get() = _binding!!

    private lateinit var database: DatabaseReference
    private var user: User? = null

    override fun onCreateView(
        inflater: LayoutInflater, container: ViewGroup?,
        savedInstanceState: Bundle?
    ): View {
        // Inflate the layout for this fragment
        _binding = FragmentHomeBinding.inflate(inflater, container, false)
        val view = binding.root
        database = Firebase.database.reference
        getProfile()

        binding.btnUpload.setOnClickListener {
            view.findNavController().navigate(R.id.action_homeFragment_to_uploadImageFragment)
        }
        binding.btnChatNow.setOnClickListener {
            view.findNavController().navigate(R.id.action_homeFragment_to_chatFragment)
        }
        binding.btnProfile.setOnClickListener {
            view.findNavController().navigate(R.id.action_homeFragment_to_profileFragment)
        }
        binding.btnRecentReports.setOnClickListener {
            view.findNavController().navigate(R.id.action_homeFragment_to_reportsFragment)
        }
        return view
    }

    override fun onDestroyView() {
        super.onDestroyView()
        _binding = null
    }

    private fun getProfile() {
        database.child("users").child(Constants.userId)
            .addValueEventListener(object : ValueEventListener {
                override fun onDataChange(snapshot: DataSnapshot) {
                    user = snapshot.getValue(User::class.java)!!
                    binding.tvUserName.text = user!!.fullName
                    Constants.user = user
                }
                override fun onCancelled(error: DatabaseError) {
                    Log.e("firebase profile", "Error getting data ${error.message}")
                }
            })
    }
}