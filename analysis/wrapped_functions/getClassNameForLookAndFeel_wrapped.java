public class LookAndFeel {
    
    public String getClassNameForLookAndFeel( String name ) {
        if ( lfNameToLookAndFeel.containsKey( name )) {
            UIManager.LookAndFeelInfo lookAndFeelInfo =
                    ( UIManager.LookAndFeelInfo ) lfNameToLookAndFeel.get( name );
            return lookAndFeelInfo.getClassName();
        }
        else {
            return null;
        }
    }
    
}