public class FScoreCalculator {
    public double fScore(ONDEXConcept x, ONDEXConcept y) {
        double recall = recall(x, y);
        double precision = precision(x, y);
        double score = 0;
        if (recall + precision != 0) {
            score = (2d * recall * precision) / (recall + precision);
        }
        return score;
    }

    private double recall(ONDEXConcept x, ONDEXConcept y) {
        // implementation of recall calculation
        return 0.0;
    }

    private double precision(ONDEXConcept x, ONDEXConcept y) {
        // implementation of precision calculation
        return 0.0;
    }
}