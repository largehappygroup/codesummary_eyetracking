public class InfluenceLawFinder {
    private List<InfluenceLaw> influenceLaws;

    public InfluenceLawFinder(List<InfluenceLaw> influenceLaws) {
        this.influenceLaws = influenceLaws;
    }

    public InfluenceLaw getApplicableLaw(Influence inf) {
        if (inf == null) {
            throw new IllegalArgumentException();
        }
        for (Iterator<InfluenceLaw> iter = influenceLaws.iterator(); iter.hasNext();) {
            InfluenceLaw infLaw = iter.next();
            if (infLaw.isApplicableTo(inf)) {
                return infLaw;
            }
        }
        return null;
    }
}