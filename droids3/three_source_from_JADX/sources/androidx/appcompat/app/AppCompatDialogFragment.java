package androidx.appcompat.app;

import android.app.Dialog;
import android.os.Bundle;
import androidx.annotation.RestrictTo;
import androidx.annotation.RestrictTo.Scope;
import androidx.fragment.app.DialogFragment;

public class AppCompatDialogFragment extends DialogFragment {
    public Dialog onCreateDialog(Bundle savedInstanceState) {
        return new AppCompatDialog(getContext(), getTheme());
    }

    @RestrictTo({Scope.LIBRARY_GROUP})
    public void setupDialog(Dialog dialog, int style) {
        if (dialog instanceof AppCompatDialog) {
            AppCompatDialog acd = (AppCompatDialog) dialog;
            if (!(style == 1 || style == 2)) {
                if (style == 3) {
                    dialog.getWindow().addFlags(24);
                } else {
                    return;
                }
            }
            acd.supportRequestWindowFeature(1);
            return;
        }
        super.setupDialog(dialog, style);
    }
}
