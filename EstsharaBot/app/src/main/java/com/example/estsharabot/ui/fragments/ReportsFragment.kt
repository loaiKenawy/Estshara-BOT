package com.example.estsharabot.ui.fragments

import android.os.Bundle
import android.util.Log
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.Toast
import androidx.fragment.app.Fragment
import androidx.recyclerview.widget.LinearLayoutManager
import androidx.recyclerview.widget.RecyclerView
import com.example.estsharabot.adapters.ReportsAdapter
import com.example.estsharabot.databinding.FragmentReportsBinding
import com.example.estsharabot.utility.Constants
import com.google.firebase.ktx.Firebase
import com.google.firebase.storage.ktx.storage
import java.io.File

class ReportsFragment : Fragment() {

    private val TAG = "ReportsFragment"

    private var _binding: FragmentReportsBinding? = null
    private val binding get() = _binding!!


    private var mList = ArrayList<String>()

    private lateinit var reportsAdapter: ReportsAdapter
    private lateinit var reportsRecyclerView: RecyclerView

    private val storage = Firebase.storage
    var storageRef = storage.reference

    // Create a reference with an initial file path and name
    val pathReference = storageRef.child("images/stars.jpg")

    // Create a reference to a file from a Google Cloud Storage URI
    val gsReference =
        storage.getReferenceFromUrl("gs://estsharabot.appspot.com/${Constants.userId}/Reports/test.pdf")

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
    }


    override fun onCreateView(
        inflater: LayoutInflater, container: ViewGroup?,
        savedInstanceState: Bundle?
    ): View? {
        _binding = FragmentReportsBinding.inflate(inflater, container, false)
        val view = binding.root

         gsReference.downloadUrl.addOnSuccessListener {
             mList.add(it.toString())
             initRecyclerView()
         }.addOnFailureListener {
             binding.rvReports.visibility = View.GONE
             binding.tvNoData.visibility = View.VISIBLE
             binding.tvNoData.text = "Can't Find Any Report"
             Toast.makeText(requireContext(),"Failed",Toast.LENGTH_LONG ).show()
         }

        return view
    }

    private fun initRecyclerView() {
        val layoutManager = LinearLayoutManager(context)
        reportsAdapter = context?.let { ReportsAdapter(it, mList,requireActivity() ) }!!
        reportsRecyclerView = binding.rvReports
        reportsRecyclerView.adapter = reportsAdapter
        reportsRecyclerView.layoutManager = layoutManager
        reportsRecyclerView.smoothScrollToPosition(mList.size - 1)

    }


}