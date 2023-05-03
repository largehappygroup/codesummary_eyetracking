public class TechnicalCommentModifier {
    public void addToTechnicalComment( final String add_to_technical_comment ) {
        if ( getTechnicalComment() != null && getTechnicalComment().length() > 0 ) {
            setTechnicalComment( getTechnicalComment() + "|n" + add_to_technical_comment );
        }
        else {
            setTechnicalComment( add_to_technical_comment );
        }
    }

    private String getTechnicalComment() {
        // implementation of getTechnicalComment()
    }

    private void setTechnicalComment(String technicalComment) {
        // implementation of setTechnicalComment()
    }
}