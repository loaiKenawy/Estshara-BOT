package com.example.estsharabot.utility

import com.example.estsharabot.model.User


class Constants {
    companion object {
        var BASE_URL = "https://4a37-102-46-41-143.ngrok-free.app/"
        var IMAGE_BASE_URL = "https://f557-102-46-41-143.ngrok-free.app/"
        const val IMAGE_UPLOAD_KEY = "postAPI"
        const val CHAT_KEY = "chatBotAPI"

        const val UPLOAD_DONE = "MRI Uploaded Successfully"
        const val ERROR_TOAST = "Failed To Upload"

        const val SUCCESS_VALUE = 1
        const val FAILED_VALUE = 0

        var userId: String = ""

        const val imageUploadFlag = "do you have any image you want to share?"

        const val loading = "loading"
        const val loaded = "loaded"

        var autoLoginFlag = true

        var user : User? = null

    }
}