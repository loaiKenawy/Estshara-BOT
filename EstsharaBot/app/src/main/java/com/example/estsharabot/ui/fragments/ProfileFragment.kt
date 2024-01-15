package com.example.estsharabot.ui.fragments

import android.os.Bundle
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import androidx.fragment.app.Fragment
import com.example.estsharabot.databinding.FragmentProfileBinding
import com.example.estsharabot.utility.Constants
import com.google.firebase.auth.ktx.auth
import com.google.firebase.ktx.Firebase


class ProfileFragment : Fragment() {


    private var _binding: FragmentProfileBinding? = null
    private val binding get() = _binding!!
    private var user = Constants.user


    override fun onCreateView(
        inflater: LayoutInflater, container: ViewGroup?,
        savedInstanceState: Bundle?
    ): View {
        _binding = FragmentProfileBinding.inflate(inflater, container, false)
        val view = binding.root
        displayProfile()
        return view
    }


    private fun displayProfile() {
        val cUser = Firebase.auth.currentUser
        binding.tvEmail.text = cUser?.email
        binding.tvUsername.text = user?.fullName
        binding.tvAge.text = user?.age.toString()
        binding.tvPhone.text = user?.phone
        binding.tvGander.text = if (user?.gander == 1) {
            "Male"
        } else {
            "Female"
        }
    }

    override fun onDestroyView() {
        super.onDestroyView()
        _binding = null
    }

}