public class PhotoSetter {

    public void setPhoto( JdaiPhoto photo ) {
        String text = null;

        if ( photo != null ) {
            label.setText( "" );
            try {
                text = photo.getSection().getInfoStore().getCaption(photo);
            } catch ( JdaiReadException e ) {
                JdaiGuiHelpers.reportException( "Unable to read caption", e );
            }
            if ( text == null || text.equals( "" ) )
                text = "No caption set";
        } else {
            label.setIcon( null );
        }
        label.setToolTipText( text );
        setNewPhoto( photo );
    } 
}