// Generated from java-escape by ANTLR 4.11.1
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link TQLParser}.
 */
public interface TQLListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link TQLParser#program}.
	 * @param ctx the parse tree
	 */
	void enterProgram(TQLParser.ProgramContext ctx);
	/**
	 * Exit a parse tree produced by {@link TQLParser#program}.
	 * @param ctx the parse tree
	 */
	void exitProgram(TQLParser.ProgramContext ctx);
	/**
	 * Enter a parse tree produced by {@link TQLParser#line}.
	 * @param ctx the parse tree
	 */
	void enterLine(TQLParser.LineContext ctx);
	/**
	 * Exit a parse tree produced by {@link TQLParser#line}.
	 * @param ctx the parse tree
	 */
	void exitLine(TQLParser.LineContext ctx);
	/**
	 * Enter a parse tree produced by {@link TQLParser#create_query}.
	 * @param ctx the parse tree
	 */
	void enterCreate_query(TQLParser.Create_queryContext ctx);
	/**
	 * Exit a parse tree produced by {@link TQLParser#create_query}.
	 * @param ctx the parse tree
	 */
	void exitCreate_query(TQLParser.Create_queryContext ctx);
	/**
	 * Enter a parse tree produced by {@link TQLParser#specifications}.
	 * @param ctx the parse tree
	 */
	void enterSpecifications(TQLParser.SpecificationsContext ctx);
	/**
	 * Exit a parse tree produced by {@link TQLParser#specifications}.
	 * @param ctx the parse tree
	 */
	void exitSpecifications(TQLParser.SpecificationsContext ctx);
	/**
	 * Enter a parse tree produced by {@link TQLParser#attributes}.
	 * @param ctx the parse tree
	 */
	void enterAttributes(TQLParser.AttributesContext ctx);
	/**
	 * Exit a parse tree produced by {@link TQLParser#attributes}.
	 * @param ctx the parse tree
	 */
	void exitAttributes(TQLParser.AttributesContext ctx);
	/**
	 * Enter a parse tree produced by {@link TQLParser#add_query}.
	 * @param ctx the parse tree
	 */
	void enterAdd_query(TQLParser.Add_queryContext ctx);
	/**
	 * Exit a parse tree produced by {@link TQLParser#add_query}.
	 * @param ctx the parse tree
	 */
	void exitAdd_query(TQLParser.Add_queryContext ctx);
	/**
	 * Enter a parse tree produced by {@link TQLParser#delete_query}.
	 * @param ctx the parse tree
	 */
	void enterDelete_query(TQLParser.Delete_queryContext ctx);
	/**
	 * Exit a parse tree produced by {@link TQLParser#delete_query}.
	 * @param ctx the parse tree
	 */
	void exitDelete_query(TQLParser.Delete_queryContext ctx);
	/**
	 * Enter a parse tree produced by {@link TQLParser#modify_query}.
	 * @param ctx the parse tree
	 */
	void enterModify_query(TQLParser.Modify_queryContext ctx);
	/**
	 * Exit a parse tree produced by {@link TQLParser#modify_query}.
	 * @param ctx the parse tree
	 */
	void exitModify_query(TQLParser.Modify_queryContext ctx);
	/**
	 * Enter a parse tree produced by {@link TQLParser#organize_query}.
	 * @param ctx the parse tree
	 */
	void enterOrganize_query(TQLParser.Organize_queryContext ctx);
	/**
	 * Exit a parse tree produced by {@link TQLParser#organize_query}.
	 * @param ctx the parse tree
	 */
	void exitOrganize_query(TQLParser.Organize_queryContext ctx);
	/**
	 * Enter a parse tree produced by {@link TQLParser#report_query}.
	 * @param ctx the parse tree
	 */
	void enterReport_query(TQLParser.Report_queryContext ctx);
	/**
	 * Exit a parse tree produced by {@link TQLParser#report_query}.
	 * @param ctx the parse tree
	 */
	void exitReport_query(TQLParser.Report_queryContext ctx);
	/**
	 * Enter a parse tree produced by {@link TQLParser#show_query}.
	 * @param ctx the parse tree
	 */
	void enterShow_query(TQLParser.Show_queryContext ctx);
	/**
	 * Exit a parse tree produced by {@link TQLParser#show_query}.
	 * @param ctx the parse tree
	 */
	void exitShow_query(TQLParser.Show_queryContext ctx);
	/**
	 * Enter a parse tree produced by {@link TQLParser#dtype}.
	 * @param ctx the parse tree
	 */
	void enterDtype(TQLParser.DtypeContext ctx);
	/**
	 * Exit a parse tree produced by {@link TQLParser#dtype}.
	 * @param ctx the parse tree
	 */
	void exitDtype(TQLParser.DtypeContext ctx);
	/**
	 * Enter a parse tree produced by {@link TQLParser#pair}.
	 * @param ctx the parse tree
	 */
	void enterPair(TQLParser.PairContext ctx);
	/**
	 * Exit a parse tree produced by {@link TQLParser#pair}.
	 * @param ctx the parse tree
	 */
	void exitPair(TQLParser.PairContext ctx);
	/**
	 * Enter a parse tree produced by {@link TQLParser#list}.
	 * @param ctx the parse tree
	 */
	void enterList(TQLParser.ListContext ctx);
	/**
	 * Exit a parse tree produced by {@link TQLParser#list}.
	 * @param ctx the parse tree
	 */
	void exitList(TQLParser.ListContext ctx);
	/**
	 * Enter a parse tree produced by {@link TQLParser#a_identifier}.
	 * @param ctx the parse tree
	 */
	void enterA_identifier(TQLParser.A_identifierContext ctx);
	/**
	 * Exit a parse tree produced by {@link TQLParser#a_identifier}.
	 * @param ctx the parse tree
	 */
	void exitA_identifier(TQLParser.A_identifierContext ctx);
	/**
	 * Enter a parse tree produced by {@link TQLParser#t_identifier}.
	 * @param ctx the parse tree
	 */
	void enterT_identifier(TQLParser.T_identifierContext ctx);
	/**
	 * Exit a parse tree produced by {@link TQLParser#t_identifier}.
	 * @param ctx the parse tree
	 */
	void exitT_identifier(TQLParser.T_identifierContext ctx);
	/**
	 * Enter a parse tree produced by {@link TQLParser#p_identifier}.
	 * @param ctx the parse tree
	 */
	void enterP_identifier(TQLParser.P_identifierContext ctx);
	/**
	 * Exit a parse tree produced by {@link TQLParser#p_identifier}.
	 * @param ctx the parse tree
	 */
	void exitP_identifier(TQLParser.P_identifierContext ctx);
	/**
	 * Enter a parse tree produced by {@link TQLParser#identifier}.
	 * @param ctx the parse tree
	 */
	void enterIdentifier(TQLParser.IdentifierContext ctx);
	/**
	 * Exit a parse tree produced by {@link TQLParser#identifier}.
	 * @param ctx the parse tree
	 */
	void exitIdentifier(TQLParser.IdentifierContext ctx);
	/**
	 * Enter a parse tree produced by {@link TQLParser#name}.
	 * @param ctx the parse tree
	 */
	void enterName(TQLParser.NameContext ctx);
	/**
	 * Exit a parse tree produced by {@link TQLParser#name}.
	 * @param ctx the parse tree
	 */
	void exitName(TQLParser.NameContext ctx);
	/**
	 * Enter a parse tree produced by {@link TQLParser#abbr}.
	 * @param ctx the parse tree
	 */
	void enterAbbr(TQLParser.AbbrContext ctx);
	/**
	 * Exit a parse tree produced by {@link TQLParser#abbr}.
	 * @param ctx the parse tree
	 */
	void exitAbbr(TQLParser.AbbrContext ctx);
}