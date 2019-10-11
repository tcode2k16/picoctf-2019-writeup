package androidx.core.widget;

import android.content.res.ColorStateList;
import android.graphics.PorterDuff.Mode;
import android.graphics.drawable.Drawable;
import android.os.Build.VERSION;
import android.util.Log;
import android.widget.CompoundButton;
import androidx.annotation.NonNull;
import androidx.annotation.Nullable;
import java.lang.reflect.Field;

public final class CompoundButtonCompat {
    private static final String TAG = "CompoundButtonCompat";
    private static Field sButtonDrawableField;
    private static boolean sButtonDrawableFieldFetched;

    private CompoundButtonCompat() {
    }

    public static void setButtonTintList(@NonNull CompoundButton button, @Nullable ColorStateList tint) {
        if (VERSION.SDK_INT >= 21) {
            button.setButtonTintList(tint);
        } else if (button instanceof TintableCompoundButton) {
            ((TintableCompoundButton) button).setSupportButtonTintList(tint);
        }
    }

    @Nullable
    public static ColorStateList getButtonTintList(@NonNull CompoundButton button) {
        if (VERSION.SDK_INT >= 21) {
            return button.getButtonTintList();
        }
        if (button instanceof TintableCompoundButton) {
            return ((TintableCompoundButton) button).getSupportButtonTintList();
        }
        return null;
    }

    public static void setButtonTintMode(@NonNull CompoundButton button, @Nullable Mode tintMode) {
        if (VERSION.SDK_INT >= 21) {
            button.setButtonTintMode(tintMode);
        } else if (button instanceof TintableCompoundButton) {
            ((TintableCompoundButton) button).setSupportButtonTintMode(tintMode);
        }
    }

    @Nullable
    public static Mode getButtonTintMode(@NonNull CompoundButton button) {
        if (VERSION.SDK_INT >= 21) {
            return button.getButtonTintMode();
        }
        if (button instanceof TintableCompoundButton) {
            return ((TintableCompoundButton) button).getSupportButtonTintMode();
        }
        return null;
    }

    @Nullable
    public static Drawable getButtonDrawable(@NonNull CompoundButton button) {
        if (VERSION.SDK_INT >= 23) {
            return button.getButtonDrawable();
        }
        boolean z = sButtonDrawableFieldFetched;
        String str = TAG;
        if (!z) {
            try {
                sButtonDrawableField = CompoundButton.class.getDeclaredField("mButtonDrawable");
                sButtonDrawableField.setAccessible(true);
            } catch (NoSuchFieldException e) {
                Log.i(str, "Failed to retrieve mButtonDrawable field", e);
            }
            sButtonDrawableFieldFetched = true;
        }
        Field field = sButtonDrawableField;
        if (field != null) {
            try {
                return (Drawable) field.get(button);
            } catch (IllegalAccessException e2) {
                Log.i(str, "Failed to get button drawable via reflection", e2);
                sButtonDrawableField = null;
            }
        }
        return null;
    }
}
