public class BalanceRankingConfigurator {
    
    public static void configBalanceRanking(List<IResponseTO> responses, String filePath) {
        PeerDAOFactory.getInstance().getAccountingDAO().loadBalancesRanking(filePath);
        long frequence = AccountingConstants.RANKING_SAVING_FREQ;

        ScheduleActionWithFixedDelayResponseTO to = new ScheduleActionWithFixedDelayResponseTO();
        to.setActionName(PeerConstants.SAVE_ACCOUNTING_ACTION_NAME);
        to.setDelay(frequence);
        to.setTimeUnit(TimeUnit.SECONDS);

        responses.add(to);
    }
}