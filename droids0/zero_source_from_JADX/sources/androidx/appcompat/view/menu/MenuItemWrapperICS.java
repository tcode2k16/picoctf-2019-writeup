package androidx.appcompat.view.menu;

import android.content.Context;
import android.content.Intent;
import android.content.res.ColorStateList;
import android.graphics.PorterDuff.Mode;
import android.graphics.drawable.Drawable;
import android.util.Log;
import android.view.ContextMenu.ContextMenuInfo;
import android.view.MenuItem;
import android.view.MenuItem.OnActionExpandListener;
import android.view.MenuItem.OnMenuItemClickListener;
import android.view.SubMenu;
import android.view.View;
import android.widget.FrameLayout;
import androidx.annotation.RestrictTo;
import androidx.annotation.RestrictTo.Scope;
import androidx.appcompat.view.CollapsibleActionView;
import androidx.core.internal.view.SupportMenuItem;
import androidx.core.view.ActionProvider;
import java.lang.reflect.Method;

@RestrictTo({Scope.LIBRARY_GROUP})
public class MenuItemWrapperICS extends BaseMenuWrapper<SupportMenuItem> implements MenuItem {
    static final String LOG_TAG = "MenuItemWrapper";
    private Method mSetExclusiveCheckableMethod;

    class ActionProviderWrapper extends ActionProvider {
        final android.view.ActionProvider mInner;

        public ActionProviderWrapper(Context context, android.view.ActionProvider inner) {
            super(context);
            this.mInner = inner;
        }

        public View onCreateActionView() {
            return this.mInner.onCreateActionView();
        }

        public boolean onPerformDefaultAction() {
            return this.mInner.onPerformDefaultAction();
        }

        public boolean hasSubMenu() {
            return this.mInner.hasSubMenu();
        }

        public void onPrepareSubMenu(SubMenu subMenu) {
            this.mInner.onPrepareSubMenu(MenuItemWrapperICS.this.getSubMenuWrapper(subMenu));
        }
    }

    static class CollapsibleActionViewWrapper extends FrameLayout implements CollapsibleActionView {
        final android.view.CollapsibleActionView mWrappedView;

        CollapsibleActionViewWrapper(View actionView) {
            super(actionView.getContext());
            this.mWrappedView = (android.view.CollapsibleActionView) actionView;
            addView(actionView);
        }

        public void onActionViewExpanded() {
            this.mWrappedView.onActionViewExpanded();
        }

        public void onActionViewCollapsed() {
            this.mWrappedView.onActionViewCollapsed();
        }

        /* access modifiers changed from: 0000 */
        public View getWrappedView() {
            return (View) this.mWrappedView;
        }
    }

    private class OnActionExpandListenerWrapper extends BaseWrapper<OnActionExpandListener> implements OnActionExpandListener {
        OnActionExpandListenerWrapper(OnActionExpandListener object) {
            super(object);
        }

        public boolean onMenuItemActionExpand(MenuItem item) {
            return ((OnActionExpandListener) this.mWrappedObject).onMenuItemActionExpand(MenuItemWrapperICS.this.getMenuItemWrapper(item));
        }

        public boolean onMenuItemActionCollapse(MenuItem item) {
            return ((OnActionExpandListener) this.mWrappedObject).onMenuItemActionCollapse(MenuItemWrapperICS.this.getMenuItemWrapper(item));
        }
    }

    private class OnMenuItemClickListenerWrapper extends BaseWrapper<OnMenuItemClickListener> implements OnMenuItemClickListener {
        OnMenuItemClickListenerWrapper(OnMenuItemClickListener object) {
            super(object);
        }

        public boolean onMenuItemClick(MenuItem item) {
            return ((OnMenuItemClickListener) this.mWrappedObject).onMenuItemClick(MenuItemWrapperICS.this.getMenuItemWrapper(item));
        }
    }

    MenuItemWrapperICS(Context context, SupportMenuItem object) {
        super(context, object);
    }

    public int getItemId() {
        return ((SupportMenuItem) this.mWrappedObject).getItemId();
    }

    public int getGroupId() {
        return ((SupportMenuItem) this.mWrappedObject).getGroupId();
    }

    public int getOrder() {
        return ((SupportMenuItem) this.mWrappedObject).getOrder();
    }

    public MenuItem setTitle(CharSequence title) {
        ((SupportMenuItem) this.mWrappedObject).setTitle(title);
        return this;
    }

    public MenuItem setTitle(int title) {
        ((SupportMenuItem) this.mWrappedObject).setTitle(title);
        return this;
    }

    public CharSequence getTitle() {
        return ((SupportMenuItem) this.mWrappedObject).getTitle();
    }

    public MenuItem setTitleCondensed(CharSequence title) {
        ((SupportMenuItem) this.mWrappedObject).setTitleCondensed(title);
        return this;
    }

    public CharSequence getTitleCondensed() {
        return ((SupportMenuItem) this.mWrappedObject).getTitleCondensed();
    }

    public MenuItem setIcon(Drawable icon) {
        ((SupportMenuItem) this.mWrappedObject).setIcon(icon);
        return this;
    }

    public MenuItem setIcon(int iconRes) {
        ((SupportMenuItem) this.mWrappedObject).setIcon(iconRes);
        return this;
    }

    public Drawable getIcon() {
        return ((SupportMenuItem) this.mWrappedObject).getIcon();
    }

    public MenuItem setIntent(Intent intent) {
        ((SupportMenuItem) this.mWrappedObject).setIntent(intent);
        return this;
    }

    public Intent getIntent() {
        return ((SupportMenuItem) this.mWrappedObject).getIntent();
    }

    public MenuItem setShortcut(char numericChar, char alphaChar) {
        ((SupportMenuItem) this.mWrappedObject).setShortcut(numericChar, alphaChar);
        return this;
    }

    public MenuItem setShortcut(char numericChar, char alphaChar, int numericModifiers, int alphaModifiers) {
        ((SupportMenuItem) this.mWrappedObject).setShortcut(numericChar, alphaChar, numericModifiers, alphaModifiers);
        return this;
    }

    public MenuItem setNumericShortcut(char numericChar) {
        ((SupportMenuItem) this.mWrappedObject).setNumericShortcut(numericChar);
        return this;
    }

    public MenuItem setNumericShortcut(char numericChar, int numericModifiers) {
        ((SupportMenuItem) this.mWrappedObject).setNumericShortcut(numericChar, numericModifiers);
        return this;
    }

    public char getNumericShortcut() {
        return ((SupportMenuItem) this.mWrappedObject).getNumericShortcut();
    }

    public int getNumericModifiers() {
        return ((SupportMenuItem) this.mWrappedObject).getNumericModifiers();
    }

    public MenuItem setAlphabeticShortcut(char alphaChar) {
        ((SupportMenuItem) this.mWrappedObject).setAlphabeticShortcut(alphaChar);
        return this;
    }

    public MenuItem setAlphabeticShortcut(char alphaChar, int alphaModifiers) {
        ((SupportMenuItem) this.mWrappedObject).setAlphabeticShortcut(alphaChar, alphaModifiers);
        return this;
    }

    public char getAlphabeticShortcut() {
        return ((SupportMenuItem) this.mWrappedObject).getAlphabeticShortcut();
    }

    public int getAlphabeticModifiers() {
        return ((SupportMenuItem) this.mWrappedObject).getAlphabeticModifiers();
    }

    public MenuItem setCheckable(boolean checkable) {
        ((SupportMenuItem) this.mWrappedObject).setCheckable(checkable);
        return this;
    }

    public boolean isCheckable() {
        return ((SupportMenuItem) this.mWrappedObject).isCheckable();
    }

    public MenuItem setChecked(boolean checked) {
        ((SupportMenuItem) this.mWrappedObject).setChecked(checked);
        return this;
    }

    public boolean isChecked() {
        return ((SupportMenuItem) this.mWrappedObject).isChecked();
    }

    public MenuItem setVisible(boolean visible) {
        return ((SupportMenuItem) this.mWrappedObject).setVisible(visible);
    }

    public boolean isVisible() {
        return ((SupportMenuItem) this.mWrappedObject).isVisible();
    }

    public MenuItem setEnabled(boolean enabled) {
        ((SupportMenuItem) this.mWrappedObject).setEnabled(enabled);
        return this;
    }

    public boolean isEnabled() {
        return ((SupportMenuItem) this.mWrappedObject).isEnabled();
    }

    public boolean hasSubMenu() {
        return ((SupportMenuItem) this.mWrappedObject).hasSubMenu();
    }

    public SubMenu getSubMenu() {
        return getSubMenuWrapper(((SupportMenuItem) this.mWrappedObject).getSubMenu());
    }

    public MenuItem setOnMenuItemClickListener(OnMenuItemClickListener menuItemClickListener) {
        ((SupportMenuItem) this.mWrappedObject).setOnMenuItemClickListener(menuItemClickListener != null ? new OnMenuItemClickListenerWrapper(menuItemClickListener) : null);
        return this;
    }

    public ContextMenuInfo getMenuInfo() {
        return ((SupportMenuItem) this.mWrappedObject).getMenuInfo();
    }

    public void setShowAsAction(int actionEnum) {
        ((SupportMenuItem) this.mWrappedObject).setShowAsAction(actionEnum);
    }

    public MenuItem setShowAsActionFlags(int actionEnum) {
        ((SupportMenuItem) this.mWrappedObject).setShowAsActionFlags(actionEnum);
        return this;
    }

    public MenuItem setActionView(View view) {
        if (view instanceof android.view.CollapsibleActionView) {
            view = new CollapsibleActionViewWrapper(view);
        }
        ((SupportMenuItem) this.mWrappedObject).setActionView(view);
        return this;
    }

    public MenuItem setActionView(int resId) {
        ((SupportMenuItem) this.mWrappedObject).setActionView(resId);
        View actionView = ((SupportMenuItem) this.mWrappedObject).getActionView();
        if (actionView instanceof android.view.CollapsibleActionView) {
            ((SupportMenuItem) this.mWrappedObject).setActionView((View) new CollapsibleActionViewWrapper(actionView));
        }
        return this;
    }

    public View getActionView() {
        View actionView = ((SupportMenuItem) this.mWrappedObject).getActionView();
        if (actionView instanceof CollapsibleActionViewWrapper) {
            return ((CollapsibleActionViewWrapper) actionView).getWrappedView();
        }
        return actionView;
    }

    public MenuItem setActionProvider(android.view.ActionProvider provider) {
        ((SupportMenuItem) this.mWrappedObject).setSupportActionProvider(provider != null ? createActionProviderWrapper(provider) : null);
        return this;
    }

    public android.view.ActionProvider getActionProvider() {
        ActionProvider provider = ((SupportMenuItem) this.mWrappedObject).getSupportActionProvider();
        if (provider instanceof ActionProviderWrapper) {
            return ((ActionProviderWrapper) provider).mInner;
        }
        return null;
    }

    public boolean expandActionView() {
        return ((SupportMenuItem) this.mWrappedObject).expandActionView();
    }

    public boolean collapseActionView() {
        return ((SupportMenuItem) this.mWrappedObject).collapseActionView();
    }

    public boolean isActionViewExpanded() {
        return ((SupportMenuItem) this.mWrappedObject).isActionViewExpanded();
    }

    public MenuItem setOnActionExpandListener(OnActionExpandListener listener) {
        ((SupportMenuItem) this.mWrappedObject).setOnActionExpandListener(listener != null ? new OnActionExpandListenerWrapper(listener) : null);
        return this;
    }

    public MenuItem setContentDescription(CharSequence contentDescription) {
        ((SupportMenuItem) this.mWrappedObject).setContentDescription(contentDescription);
        return this;
    }

    public CharSequence getContentDescription() {
        return ((SupportMenuItem) this.mWrappedObject).getContentDescription();
    }

    public MenuItem setTooltipText(CharSequence tooltipText) {
        ((SupportMenuItem) this.mWrappedObject).setTooltipText(tooltipText);
        return this;
    }

    public CharSequence getTooltipText() {
        return ((SupportMenuItem) this.mWrappedObject).getTooltipText();
    }

    public MenuItem setIconTintList(ColorStateList tint) {
        ((SupportMenuItem) this.mWrappedObject).setIconTintList(tint);
        return this;
    }

    public ColorStateList getIconTintList() {
        return ((SupportMenuItem) this.mWrappedObject).getIconTintList();
    }

    public MenuItem setIconTintMode(Mode tintMode) {
        ((SupportMenuItem) this.mWrappedObject).setIconTintMode(tintMode);
        return this;
    }

    public Mode getIconTintMode() {
        return ((SupportMenuItem) this.mWrappedObject).getIconTintMode();
    }

    public void setExclusiveCheckable(boolean checkable) {
        try {
            if (this.mSetExclusiveCheckableMethod == null) {
                this.mSetExclusiveCheckableMethod = ((SupportMenuItem) this.mWrappedObject).getClass().getDeclaredMethod("setExclusiveCheckable", new Class[]{Boolean.TYPE});
            }
            this.mSetExclusiveCheckableMethod.invoke(this.mWrappedObject, new Object[]{Boolean.valueOf(checkable)});
        } catch (Exception e) {
            Log.w(LOG_TAG, "Error while calling setExclusiveCheckable", e);
        }
    }

    /* access modifiers changed from: 0000 */
    public ActionProviderWrapper createActionProviderWrapper(android.view.ActionProvider provider) {
        return new ActionProviderWrapper(this.mContext, provider);
    }
}
