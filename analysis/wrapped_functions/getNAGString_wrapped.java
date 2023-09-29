public class NAGStringParser {
   public String getNAGString(boolean allNumeric) {
      if (nags == null)
         return null;
      StringBuilder sb = new StringBuilder();
      String suff = null;
      int count = 0;
      for (int i = 0; i < nags.length; i++) {
         suff = NAG.numberToString(nags[i], allNumeric);
         if (suff != null) {
            if (count++ > 0)
               sb.append(" ");
            sb.append(suff);
         }
      }
      return sb.toString();
   }
}