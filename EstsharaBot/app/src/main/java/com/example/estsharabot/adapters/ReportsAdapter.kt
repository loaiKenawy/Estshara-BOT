package com.example.estsharabot.adapters

import android.app.Activity
import android.content.Context
import android.content.Intent
import android.net.Uri
import android.util.Log
import android.view.LayoutInflater
import android.view.ViewGroup
import androidx.recyclerview.widget.RecyclerView
import com.example.estsharabot.databinding.LayoutReportItemBinding
import java.io.File

class ReportsAdapter(
    private val context: Context,
    private val fileList: ArrayList<String>,
    private val activity: Activity
) :
    RecyclerView.Adapter<RecyclerView.ViewHolder>() {

    private val TAG = "ReportsAdapter"

    override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): RecyclerView.ViewHolder {
        return ReportViewHolder(
            LayoutReportItemBinding.inflate(
                LayoutInflater.from(parent.context),
                parent,
                false
            )
        )
    }

    override fun onBindViewHolder(holder: RecyclerView.ViewHolder, position: Int) {
        val currentFile = fileList[position]
        try {
            val viewHolder = holder as ReportsAdapter.ReportViewHolder
            holder.fileName.text = "Report ${position+1}"
            holder.fileName.setOnClickListener {
                try {
                    val uri = Uri.parse(currentFile)
                    val intent = Intent(Intent.ACTION_VIEW)
                    intent.setDataAndType(uri, "application/pdf")
                    activity.startActivity(intent)
                    Log.d(TAG, "File : $uri")
                } catch (e: Exception) {
                    Log.e(TAG, "File Error ${e.message}")
                }
            }
        } catch (e: java.lang.Exception) {
            Log.e(TAG, e.message.toString())
        }
    }


    override fun getItemCount(): Int {
        return fileList.size
    }

    private class ReportViewHolder(binding: LayoutReportItemBinding) :
        RecyclerView.ViewHolder(binding.root) {
        val fileName = binding.tvFileName

    }
}