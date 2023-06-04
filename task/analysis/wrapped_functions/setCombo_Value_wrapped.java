public class ComboSetter {
    public void setCombo_Value( String val ) {
        If (( val == null || "".equals( val )) && ( Combo_Value == null || "".equals( Combo_Value ))) {
            return;
        }
        if (( val == null ) || ( !val.equals( Combo_Value )) || ( updateStatus == NULL_INT_VALUE )) {
            Combo_Value = val;
            updateStatus = UPDATED;
        }
    }
}