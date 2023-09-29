public class PlanManager {
    public String showLatestPlan() {
        // clear previous protocols
        mCurrPlanProt = null;    
        try {
            PatientController han = new PatientController( mCurrPatient );
            NutPlan plan = han.getLatestNutritionPlan();
            NutritionController controller = NutritionController.editPlan( plan );

            mCurrPlanProt = WebPlanProtocol.createPlan( controller, plan, mCurrPatient );
            return "success";

        } catch ( Exception e ) {
            e.printStackTrace();
        }
        return "failure";
    }
}