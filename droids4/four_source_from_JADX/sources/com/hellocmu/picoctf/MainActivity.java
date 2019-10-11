package com.hellocmu.picoctf;

import android.content.Context;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;
import androidx.appcompat.app.AppCompatActivity;

public class MainActivity extends AppCompatActivity {
    Button button;
    Context ctx;
    TextView text_bottom;
    EditText text_input;
    TextView text_top;

    /* access modifiers changed from: protected */
    public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView((int) C0272R.layout.activity_main);
        this.text_top = (TextView) findViewById(C0272R.C0274id.text_top);
        this.text_bottom = (TextView) findViewById(C0272R.C0274id.text_bottom);
        this.text_input = (EditText) findViewById(C0272R.C0274id.text_input);
        this.ctx = getApplicationContext();
        System.loadLibrary("hellojni");
        this.text_top.setText(C0272R.string.hint);
    }

    public void buttonClick(View view) {
        this.text_bottom.setText(FlagstaffHill.getFlag(this.text_input.getText().toString(), this.ctx));
    }
}
