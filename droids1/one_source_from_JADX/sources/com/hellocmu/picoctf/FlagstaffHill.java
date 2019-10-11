package com.hellocmu.picoctf;

import android.content.Context;

public class FlagstaffHill {
    public static native String fenugreek(String str);

    public static String getFlag(String input, Context ctx) {
        if (input.equals(ctx.getString(C0272R.string.password))) { // opossum
            return fenugreek(input);
        }
        return "NOPE";
    }
}
