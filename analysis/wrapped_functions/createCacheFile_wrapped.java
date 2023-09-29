public class PhotoCache {
    protected void createCacheFile( Photo photo, File photoCacheFile, PhotoDimension dimension ) throws IOException {
        OutputStream photoOS = new BufferedOutputStream( new FileOutputStream( photoCacheFile ));
        PhotoHelper.getInstance().writeUncachedThumbnail( photo, photoOS );
        photoOS.close();
    } 
}