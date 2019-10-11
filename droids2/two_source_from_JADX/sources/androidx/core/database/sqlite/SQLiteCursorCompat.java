package androidx.core.database.sqlite;

import android.database.sqlite.SQLiteCursor;
import android.os.Build.VERSION;
import androidx.annotation.NonNull;

public final class SQLiteCursorCompat {
    private SQLiteCursorCompat() {
    }

    public static void setFillWindowForwardOnly(@NonNull SQLiteCursor cursor, boolean fillWindowForwardOnly) {
        if (VERSION.SDK_INT >= 28) {
            cursor.setFillWindowForwardOnly(fillWindowForwardOnly);
        }
    }
}
