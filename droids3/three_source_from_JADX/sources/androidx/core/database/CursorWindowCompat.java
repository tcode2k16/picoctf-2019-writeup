package androidx.core.database;

import android.database.CursorWindow;
import android.os.Build.VERSION;
import androidx.annotation.NonNull;
import androidx.annotation.Nullable;

public final class CursorWindowCompat {
    private CursorWindowCompat() {
    }

    @NonNull
    public static CursorWindow create(@Nullable String name, long windowSizeBytes) {
        if (VERSION.SDK_INT >= 28) {
            return new CursorWindow(name, windowSizeBytes);
        }
        if (VERSION.SDK_INT >= 15) {
            return new CursorWindow(name);
        }
        return new CursorWindow(false);
    }
}
