package androidx.lifecycle;

import androidx.annotation.RestrictTo;
import androidx.annotation.RestrictTo.Scope;
import androidx.lifecycle.Lifecycle.Event;

@RestrictTo({Scope.LIBRARY_GROUP})
public class SingleGeneratedAdapterObserver implements GenericLifecycleObserver {
    private final GeneratedAdapter mGeneratedAdapter;

    SingleGeneratedAdapterObserver(GeneratedAdapter generatedAdapter) {
        this.mGeneratedAdapter = generatedAdapter;
    }

    public void onStateChanged(LifecycleOwner source, Event event) {
        this.mGeneratedAdapter.callMethods(source, event, false, null);
        this.mGeneratedAdapter.callMethods(source, event, true, null);
    }
}
