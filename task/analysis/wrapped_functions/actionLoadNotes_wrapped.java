public class NotesLoader {
    private void actionLoadNotes() {
        enableUserActions( false );
    
        // set focus, otherwise it gives focus to "clear" >> scary/not wanted
        multiSubmitButton.requestFocusInWindow();
    
        resetSingleTextFields();
        multipleGUIList.clearSelection();
        multipleResources = loadNotesFile();
        updateMultiList();
        enableUserActions( true );
    }
}