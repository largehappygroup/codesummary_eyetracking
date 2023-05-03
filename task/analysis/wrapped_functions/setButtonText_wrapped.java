public class ButtonTextSetter {
    
    private MenuItem menuItem;
    
    public ButtonTextSetter(MenuItem menuItem) {
        this.menuItem = menuItem;
    }
    
    private void setButtonText() {
        String txt = menuItem.getTitle() + " (" + menuItem.getStock() + " in Stock)";
        try {
            Course tmpCourse = ( Course )menuItem;

            if ( tmpCourse.getCourseType() == Course.FIRST_COURSE ) {
                txt = "1st: " + txt;
            } else {
                txt = "2nd: " + txt;
            }
        } catch ( Exception e ) {
            // TODO: handle exception
        }
        this.setText( txt );
    }
}