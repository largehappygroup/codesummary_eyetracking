public class ResponseModifier {

    private static final String CACHE_CONTROL_HEADER = "Cache-Control";
    private static final SimpleDateFormat DATE_FORMAT = new SimpleDateFormat("EEE, dd MMM yyyy HH:mm:ss zzz", Locale.US);

    public void addRelativeHeaders(Response response, int timeInSeconds) {
        response.setHeader(CACHE_CONTROL_HEADER, String.format("max-age=%d", timeInSeconds));
        Calendar expires = Calendar.getInstance();
        expires.add(Calendar.SECOND, timeInSeconds);
        response.setHeader("Expires", DATE_FORMAT.format(expires.getTime()));
    }
}