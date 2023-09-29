public class RedundantOperationsRemover {
    private void removeRedundantOperations( OBEXElement file, List< OBEXElement > filesToRemove ) {
        OBEXElement parentFolder = file;
        log.debug( "Removing redundant operations" );

        while (( parentFolder = parentFolder.getParent() ) != null ) {
            if ( filesToRemove.contains( parentFolder )) {
                filesToRemove.remove( file );
                file = parentFolder;
            }
        }
    }
}