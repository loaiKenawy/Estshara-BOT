package com.example.estsharabot.utility

import android.app.AlertDialog
import android.app.Dialog
import android.os.Bundle
import androidx.fragment.app.DialogFragment
import com.example.estsharabot.ui.fragments.ChatFragment

class BackPressedDialog() : DialogFragment() {
    companion object {
        var waitFlag: String? = null
    }
    override fun onCreateDialog(savedInstanceState: Bundle?): Dialog =
        AlertDialog.Builder(requireContext())
            .setMessage("You are going to discard this session")
            .setPositiveButton("Discard") { _, _ ->
                waitFlag = "Discard"
            }
            .setNegativeButton("Stay") { _, _ ->
                waitFlag = "Stay"
            }
            .create()
}