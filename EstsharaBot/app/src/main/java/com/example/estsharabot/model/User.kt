package com.example.estsharabot.model

import com.google.firebase.database.Exclude


data class User(
    var fullName: String? = null,
    var phone: String? = null,
    var age: Int? = null,
    var gander: Int? = null
) {


}