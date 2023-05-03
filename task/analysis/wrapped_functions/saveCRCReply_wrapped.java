public class SaveCRCReply {
    private void saveCRCReply(ClientRemoteContainerReply crcReply) {	
        LoadService.currentlyWritingFile = true;
        String mySavingPath = LoadService.SERVICE_NODE_DESCRIPTION_FILE;
        try {
            ObjectOutputStream out = new ObjectOutputStream(new FileOutputStream(mySavingPath));
            out.writeObject(crcReply);
            out.flush();
            out.close();	
        } catch (FileNotFoundException e1) {
            e1.printStackTrace();
        } catch (IOException e1) {
            e1.printStackTrace();
        }
        LoadService.currentlyWritingFile = false;
    }
}