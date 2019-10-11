package androidx.appcompat.widget;

import android.os.Build.VERSION;
import android.view.View;
import androidx.annotation.NonNull;
import androidx.annotation.Nullable;

public class TooltipCompat {
    public static void setTooltipText(@NonNull View view, @Nullable CharSequence tooltipText) {
        if (VERSION.SDK_INT >= 26) {
            view.setTooltipText(tooltipText);
        } else {
            TooltipCompatHandler.setTooltipText(view, tooltipText);
        }
    }

    private TooltipCompat() {
    }
}
