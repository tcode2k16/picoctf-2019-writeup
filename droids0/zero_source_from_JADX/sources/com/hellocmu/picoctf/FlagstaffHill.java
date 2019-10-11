package com.hellocmu.picoctf;

import android.content.Context;
import android.util.Log;

public class FlagstaffHill {
    public static native String paprika(String str);

    public static String getFlag(String input, Context ctx) {
        Log.i("PICO", paprika(input));
        return "Not Today...";
    }
}
