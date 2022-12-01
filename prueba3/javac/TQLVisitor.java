// Generated from java-escape by ANTLR 4.11.1
import org.antlr.v4.runtime.tree.ParseTreeVisitor;

/**
 * This interface defines a complete generic visitor for a parse tree produced
 * by {@link TQLParser}.
 *
 * @param <T> The return type of the visit operation. Use {@link Void} for
 * operations with no return type.
 */
public interface TQLVisitor<T> extends ParseTreeVisitor<T> {
	/**
	 * Visit a parse tree produced by {@link TQLParser#program}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitProgram(TQLParser.ProgramContext ctx);
	/**
	 * Visit a parse tree produced by {@link TQLParser#line}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitLine(TQLParser.LineContext ctx);
	/**
	 * Visit a parse tree produced by {@link TQLParser#create_query}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitCreate_query(TQLParser.Create_queryContext ctx);
	/**
	 * Visit a parse tree produced by {@link TQLParser#specifications}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitSpecifications(TQLParser.SpecificationsContext ctx);
	/**
	 * Visit a parse tree produced by {@link TQLParser#attributes}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitAttributes(TQLParser.AttributesContext ctx);
	/**
	 * Visit a parse tree produced by {@link TQLParser#add_query}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitAdd_query(TQLParser.Add_queryContext ctx);
	/**
	 * Visit a parse tree produced by {@link TQLParser#delete_query}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitDelete_query(TQLParser.Delete_queryContext ctx);
	/**
	 * Visit a parse tree produced by {@link TQLParser#modify_query}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitModify_query(TQLParser.Modify_queryContext ctx);
	/**
	 * Visit a parse tree produced by {@link TQLParser#organize_query}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitOrganize_query(TQLParser.Organize_queryContext ctx);
	/**
	 * Visit a parse tree produced by {@link TQLParser#report_query}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitReport_query(TQLParser.Report_queryContext ctx);
	/**
	 * Visit a parse tree produced by {@link TQLParser#show_query}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitShow_query(TQLParser.Show_queryContext ctx);
	/**
	 * Visit a parse tree produced by {@link TQLParser#dtype}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitDtype(TQLParser.DtypeContext ctx);
	/**
	 * Visit a parse tree produced by {@link TQLParser#pair}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitPair(TQLParser.PairContext ctx);
	/**
	 * Visit a parse tree produced by {@link TQLParser#list}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitList(TQLParser.ListContext ctx);
	/**
	 * Visit a parse tree produced by {@link TQLParser#a_identifier}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitA_identifier(TQLParser.A_identifierContext ctx);
	/**
	 * Visit a parse tree produced by {@link TQLParser#t_identifier}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitT_identifier(TQLParser.T_identifierContext ctx);
	/**
	 * Visit a parse tree produced by {@link TQLParser#p_identifier}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitP_identifier(TQLParser.P_identifierContext ctx);
	/**
	 * Visit a parse tree produced by {@link TQLParser#identifier}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitIdentifier(TQLParser.IdentifierContext ctx);
	/**
	 * Visit a parse tree produced by {@link TQLParser#name}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitName(TQLParser.NameContext ctx);
	/**
	 * Visit a parse tree produced by {@link TQLParser#abbr}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitAbbr(TQLParser.AbbrContext ctx);
}