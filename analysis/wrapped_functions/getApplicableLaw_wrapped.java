import java.util.Iterator;

public class MyClass {
    // Assuming influenceLaws is a collection of InfluenceLaw
    Iterable<InfluenceLaw> influenceLaws;

    public InfluenceLaw getApplicableLaw(Influence inf) {
        if (inf == null) {
            throw new IllegalArgumentException();
        }
        for (Iterator iter = influenceLaws.iterator(); iter.hasNext(); ) {
            InfluenceLaw infLaw = (InfluenceLaw) iter.next();
            if(infLaw.isApplicableTo(inf)) {
                return infLaw;
            }
        }
        return null;
    }
    
    // Placeholder class definitions, replace these with your actual class definitions
    class Influence {
        // Your Influence class implementation goes here
    }

    class InfluenceLaw {
        // Your InfluenceLaw class implementation goes here
        boolean isApplicableTo(Influence influence) {
            // Replace this with your actual implementation
            return false;
        }
    }
}