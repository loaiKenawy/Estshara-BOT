package com.example.estsharabot.remote

import android.util.Log
import com.example.estsharabot.utility.Constants
import okhttp3.OkHttpClient
import retrofit2.Retrofit
import retrofit2.converter.gson.GsonConverterFactory
import java.util.concurrent.TimeUnit


class Service {

    companion object {

        var methods: ApiMethods? = null
        var methods2: ApiMethods? = null
        private val okHttpClient: OkHttpClient = OkHttpClient().newBuilder()
            .connectTimeout(60, TimeUnit.SECONDS)
            .readTimeout(60, TimeUnit.SECONDS)
            .writeTimeout(60, TimeUnit.SECONDS)
            .build()
        fun getInstance() : ApiMethods? {
            if (methods == null) {
                val baseURL = Constants.BASE_URL
                val retrofit = Retrofit.Builder()
                    .baseUrl(baseURL)
                    .addConverterFactory(GsonConverterFactory.create())
                    .client(okHttpClient)
                    .build()
                methods = retrofit.create(ApiMethods::class.java)
            }
            return methods
        }

        fun getInstance2() : ApiMethods?{
            if (methods2 == null) {
                val baseURL = Constants.IMAGE_BASE_URL
                val retrofit = Retrofit.Builder()
                    .baseUrl(baseURL)
                    .addConverterFactory(GsonConverterFactory.create())
                    .client(okHttpClient)
                    .build()
                methods2 = retrofit.create(ApiMethods::class.java)
            }
            return methods2
        }
    }
}