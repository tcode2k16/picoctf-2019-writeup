package androidx.core.graphics;

import android.content.Context;
import android.content.res.Resources;
import android.os.Process;
import android.os.StrictMode;
import android.os.StrictMode.ThreadPolicy;
import android.util.Log;
import androidx.annotation.Nullable;
import androidx.annotation.RequiresApi;
import androidx.annotation.RestrictTo;
import androidx.annotation.RestrictTo.Scope;
import java.io.Closeable;
import java.io.File;
import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.nio.ByteBuffer;
import java.nio.MappedByteBuffer;
import java.nio.channels.FileChannel;
import java.nio.channels.FileChannel.MapMode;

@RestrictTo({Scope.LIBRARY_GROUP})
public class TypefaceCompatUtil {
    private static final String CACHE_FILE_PREFIX = ".font";
    private static final String TAG = "TypefaceCompatUtil";

    private TypefaceCompatUtil() {
    }

    @Nullable
    public static File getTempFile(Context context) {
        StringBuilder sb = new StringBuilder();
        sb.append(CACHE_FILE_PREFIX);
        sb.append(Process.myPid());
        String str = "-";
        sb.append(str);
        sb.append(Process.myTid());
        sb.append(str);
        String prefix = sb.toString();
        int i = 0;
        while (i < 100) {
            File cacheDir = context.getCacheDir();
            StringBuilder sb2 = new StringBuilder();
            sb2.append(prefix);
            sb2.append(i);
            File file = new File(cacheDir, sb2.toString());
            try {
                if (file.createNewFile()) {
                    return file;
                }
                i++;
            } catch (IOException e) {
            }
        }
        return null;
    }

    @RequiresApi(19)
    @Nullable
    private static ByteBuffer mmap(File file) {
        Throwable th;
        Throwable th2;
        try {
            FileInputStream fis = new FileInputStream(file);
            try {
                FileChannel channel = fis.getChannel();
                MappedByteBuffer map = channel.map(MapMode.READ_ONLY, 0, channel.size());
                fis.close();
                return map;
            } catch (Throwable th3) {
                Throwable th4 = th3;
                th = r2;
                th2 = th4;
            }
            throw th2;
            if (th != null) {
                try {
                    fis.close();
                } catch (Throwable th5) {
                    th.addSuppressed(th5);
                }
            } else {
                fis.close();
            }
            throw th2;
        } catch (IOException e) {
            return null;
        }
    }

    /* JADX WARNING: Code restructure failed: missing block: B:32:0x004e, code lost:
        r3 = th;
     */
    /* JADX WARNING: Code restructure failed: missing block: B:33:0x004f, code lost:
        r4 = null;
     */
    /* JADX WARNING: Code restructure failed: missing block: B:37:0x0053, code lost:
        r4 = move-exception;
     */
    /* JADX WARNING: Code restructure failed: missing block: B:38:0x0054, code lost:
        r10 = r4;
        r4 = r3;
        r3 = r10;
     */
    /* JADX WARNING: Failed to process nested try/catch */
    /* JADX WARNING: Removed duplicated region for block: B:32:0x004e A[ExcHandler: all (th java.lang.Throwable), Splitter:B:7:0x0014] */
    @androidx.annotation.RequiresApi(19)
    @androidx.annotation.Nullable
    /* Code decompiled incorrectly, please refer to instructions dump. */
    public static java.nio.ByteBuffer mmap(android.content.Context r11, android.os.CancellationSignal r12, android.net.Uri r13) {
        /*
            android.content.ContentResolver r0 = r11.getContentResolver()
            r1 = 0
            java.lang.String r2 = "r"
            android.os.ParcelFileDescriptor r2 = r0.openFileDescriptor(r13, r2, r12)     // Catch:{ IOException -> 0x0068 }
            if (r2 != 0) goto L_0x0014
            if (r2 == 0) goto L_0x0013
            r2.close()     // Catch:{ IOException -> 0x0068 }
        L_0x0013:
            return r1
        L_0x0014:
            java.io.FileInputStream r3 = new java.io.FileInputStream     // Catch:{ Throwable -> 0x0051, all -> 0x004e }
            java.io.FileDescriptor r4 = r2.getFileDescriptor()     // Catch:{ Throwable -> 0x0051, all -> 0x004e }
            r3.<init>(r4)     // Catch:{ Throwable -> 0x0051, all -> 0x004e }
            java.nio.channels.FileChannel r4 = r3.getChannel()     // Catch:{ Throwable -> 0x0039, all -> 0x0036 }
            long r8 = r4.size()     // Catch:{ Throwable -> 0x0039, all -> 0x0036 }
            java.nio.channels.FileChannel$MapMode r5 = java.nio.channels.FileChannel.MapMode.READ_ONLY     // Catch:{ Throwable -> 0x0039, all -> 0x0036 }
            r6 = 0
            java.nio.MappedByteBuffer r5 = r4.map(r5, r6, r8)     // Catch:{ Throwable -> 0x0039, all -> 0x0036 }
            r3.close()     // Catch:{ Throwable -> 0x0051, all -> 0x004e }
            if (r2 == 0) goto L_0x0035
            r2.close()     // Catch:{ IOException -> 0x0068 }
        L_0x0035:
            return r5
        L_0x0036:
            r4 = move-exception
            r5 = r1
            goto L_0x003f
        L_0x0039:
            r4 = move-exception
            throw r4     // Catch:{ all -> 0x003b }
        L_0x003b:
            r5 = move-exception
            r10 = r5
            r5 = r4
            r4 = r10
        L_0x003f:
            if (r5 == 0) goto L_0x004a
            r3.close()     // Catch:{ Throwable -> 0x0045, all -> 0x004e }
            goto L_0x004d
        L_0x0045:
            r6 = move-exception
            r5.addSuppressed(r6)     // Catch:{ Throwable -> 0x0051, all -> 0x004e }
            goto L_0x004d
        L_0x004a:
            r3.close()     // Catch:{ Throwable -> 0x0051, all -> 0x004e }
        L_0x004d:
            throw r4     // Catch:{ Throwable -> 0x0051, all -> 0x004e }
        L_0x004e:
            r3 = move-exception
            r4 = r1
            goto L_0x0057
        L_0x0051:
            r3 = move-exception
            throw r3     // Catch:{ all -> 0x0053 }
        L_0x0053:
            r4 = move-exception
            r10 = r4
            r4 = r3
            r3 = r10
        L_0x0057:
            if (r2 == 0) goto L_0x0067
            if (r4 == 0) goto L_0x0064
            r2.close()     // Catch:{ Throwable -> 0x005f }
            goto L_0x0067
        L_0x005f:
            r5 = move-exception
            r4.addSuppressed(r5)     // Catch:{ IOException -> 0x0068 }
            goto L_0x0067
        L_0x0064:
            r2.close()     // Catch:{ IOException -> 0x0068 }
        L_0x0067:
            throw r3     // Catch:{ IOException -> 0x0068 }
        L_0x0068:
            r2 = move-exception
            return r1
        */
        throw new UnsupportedOperationException("Method not decompiled: androidx.core.graphics.TypefaceCompatUtil.mmap(android.content.Context, android.os.CancellationSignal, android.net.Uri):java.nio.ByteBuffer");
    }

    @RequiresApi(19)
    @Nullable
    public static ByteBuffer copyToDirectBuffer(Context context, Resources res, int id) {
        File tmpFile = getTempFile(context);
        ByteBuffer byteBuffer = null;
        if (tmpFile == null) {
            return null;
        }
        try {
            if (copyToFile(tmpFile, res, id)) {
                byteBuffer = mmap(tmpFile);
            }
            return byteBuffer;
        } finally {
            tmpFile.delete();
        }
    }

    public static boolean copyToFile(File file, InputStream is) {
        FileOutputStream os = null;
        ThreadPolicy old = StrictMode.allowThreadDiskWrites();
        try {
            os = new FileOutputStream(file, false);
            byte[] buffer = new byte[1024];
            while (true) {
                int read = is.read(buffer);
                int readLen = read;
                if (read != -1) {
                    os.write(buffer, 0, readLen);
                } else {
                    return true;
                }
            }
        } catch (IOException e) {
            String str = TAG;
            StringBuilder sb = new StringBuilder();
            sb.append("Error copying resource contents to temp file: ");
            sb.append(e.getMessage());
            Log.e(str, sb.toString());
            return false;
        } finally {
            closeQuietly(os);
            StrictMode.setThreadPolicy(old);
        }
    }

    public static boolean copyToFile(File file, Resources res, int id) {
        InputStream is = null;
        try {
            is = res.openRawResource(id);
            return copyToFile(file, is);
        } finally {
            closeQuietly(is);
        }
    }

    public static void closeQuietly(Closeable c) {
        if (c != null) {
            try {
                c.close();
            } catch (IOException e) {
            }
        }
    }
}
