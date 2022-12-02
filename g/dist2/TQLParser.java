// Generated from java-escape by ANTLR 4.11.1
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue"})
public class TQLParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.11.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, T__2=3, T__3=4, T__4=5, T__5=6, T__6=7, T__7=8, CREATE=9, 
		TOURNAMENT=10, WITH=11, PARTICIPANT=12, ADD=13, TO=14, ORGANIZE=15, ATTRIBUTE=16, 
		DELETE=17, FROM=18, BY=19, REPORT=20, MODIFY=21, MATCH=22, OF=23, ID=24, 
		SHOW=25, PHASE=26, SUMMARY=27, TEAM=28, PLAYER=29, CONTENDER=30, STRING=31, 
		WORD=32, INTEGER=33, WHITESPACE=34;
	public static final int
		RULE_program = 0, RULE_line = 1, RULE_create_query = 2, RULE_specifications = 3, 
		RULE_attributes = 4, RULE_add_query = 5, RULE_delete_query = 6, RULE_modify_query = 7, 
		RULE_organize_query = 8, RULE_report_query = 9, RULE_show_query = 10, 
		RULE_dtype = 11, RULE_pair = 12, RULE_list = 13, RULE_a_identifier = 14, 
		RULE_t_identifier = 15, RULE_p_identifier = 16, RULE_identifier = 17, 
		RULE_name = 18, RULE_abbr = 19;
	private static String[] makeRuleNames() {
		return new String[] {
			"program", "line", "create_query", "specifications", "attributes", "add_query", 
			"delete_query", "modify_query", "organize_query", "report_query", "show_query", 
			"dtype", "pair", "list", "a_identifier", "t_identifier", "p_identifier", 
			"identifier", "name", "abbr"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'('", "','", "')'", "'{'", "'}'", "':'", "'['", "']'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, null, null, null, null, null, null, null, null, "CREATE", "TOURNAMENT", 
			"WITH", "PARTICIPANT", "ADD", "TO", "ORGANIZE", "ATTRIBUTE", "DELETE", 
			"FROM", "BY", "REPORT", "MODIFY", "MATCH", "OF", "ID", "SHOW", "PHASE", 
			"SUMMARY", "TEAM", "PLAYER", "CONTENDER", "STRING", "WORD", "INTEGER", 
			"WHITESPACE"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}

	@Override
	public String getGrammarFileName() { return "java-escape"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public TQLParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ProgramContext extends ParserRuleContext {
		public List<LineContext> line() {
			return getRuleContexts(LineContext.class);
		}
		public LineContext line(int i) {
			return getRuleContext(LineContext.class,i);
		}
		public ProgramContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_program; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof TQLListener ) ((TQLListener)listener).enterProgram(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof TQLListener ) ((TQLListener)listener).exitProgram(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof TQLVisitor ) return ((TQLVisitor<? extends T>)visitor).visitProgram(this);
			else return visitor.visitChildren(this);
		}
	}

	public final ProgramContext program() throws RecognitionException {
		ProgramContext _localctx = new ProgramContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_program);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(41); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(40);
				line();
				}
				}
				setState(43); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( ((_la) & ~0x3f) == 0 && ((1L << _la) & 36872704L) != 0 );
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class LineContext extends ParserRuleContext {
		public Create_queryContext create_query() {
			return getRuleContext(Create_queryContext.class,0);
		}
		public Add_queryContext add_query() {
			return getRuleContext(Add_queryContext.class,0);
		}
		public Delete_queryContext delete_query() {
			return getRuleContext(Delete_queryContext.class,0);
		}
		public Modify_queryContext modify_query() {
			return getRuleContext(Modify_queryContext.class,0);
		}
		public Organize_queryContext organize_query() {
			return getRuleContext(Organize_queryContext.class,0);
		}
		public Report_queryContext report_query() {
			return getRuleContext(Report_queryContext.class,0);
		}
		public Show_queryContext show_query() {
			return getRuleContext(Show_queryContext.class,0);
		}
		public LineContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_line; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof TQLListener ) ((TQLListener)listener).enterLine(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof TQLListener ) ((TQLListener)listener).exitLine(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof TQLVisitor ) return ((TQLVisitor<? extends T>)visitor).visitLine(this);
			else return visitor.visitChildren(this);
		}
	}

	public final LineContext line() throws RecognitionException {
		LineContext _localctx = new LineContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_line);
		try {
			setState(52);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case CREATE:
				enterOuterAlt(_localctx, 1);
				{
				setState(45);
				create_query();
				}
				break;
			case ADD:
				enterOuterAlt(_localctx, 2);
				{
				setState(46);
				add_query();
				}
				break;
			case DELETE:
				enterOuterAlt(_localctx, 3);
				{
				setState(47);
				delete_query();
				}
				break;
			case MODIFY:
				enterOuterAlt(_localctx, 4);
				{
				setState(48);
				modify_query();
				}
				break;
			case ORGANIZE:
				enterOuterAlt(_localctx, 5);
				{
				setState(49);
				organize_query();
				}
				break;
			case REPORT:
				enterOuterAlt(_localctx, 6);
				{
				setState(50);
				report_query();
				}
				break;
			case SHOW:
				enterOuterAlt(_localctx, 7);
				{
				setState(51);
				show_query();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Create_queryContext extends ParserRuleContext {
		public TerminalNode CREATE() { return getToken(TQLParser.CREATE, 0); }
		public TerminalNode TOURNAMENT() { return getToken(TQLParser.TOURNAMENT, 0); }
		public NameContext name() {
			return getRuleContext(NameContext.class,0);
		}
		public SpecificationsContext specifications() {
			return getRuleContext(SpecificationsContext.class,0);
		}
		public Create_queryContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_create_query; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof TQLListener ) ((TQLListener)listener).enterCreate_query(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof TQLListener ) ((TQLListener)listener).exitCreate_query(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof TQLVisitor ) return ((TQLVisitor<? extends T>)visitor).visitCreate_query(this);
			else return visitor.visitChildren(this);
		}
	}

	public final Create_queryContext create_query() throws RecognitionException {
		Create_queryContext _localctx = new Create_queryContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_create_query);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(54);
			match(CREATE);
			setState(55);
			match(TOURNAMENT);
			setState(56);
			name();
			setState(58);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,2,_ctx) ) {
			case 1:
				{
				setState(57);
				specifications();
				}
				break;
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class SpecificationsContext extends ParserRuleContext {
		public AttributesContext attributes() {
			return getRuleContext(AttributesContext.class,0);
		}
		public TerminalNode WITH() { return getToken(TQLParser.WITH, 0); }
		public TerminalNode INTEGER() { return getToken(TQLParser.INTEGER, 0); }
		public TerminalNode PARTICIPANT() { return getToken(TQLParser.PARTICIPANT, 0); }
		public ListContext list() {
			return getRuleContext(ListContext.class,0);
		}
		public TerminalNode CONTENDER() { return getToken(TQLParser.CONTENDER, 0); }
		public TerminalNode TEAM() { return getToken(TQLParser.TEAM, 0); }
		public TerminalNode PLAYER() { return getToken(TQLParser.PLAYER, 0); }
		public SpecificationsContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_specifications; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof TQLListener ) ((TQLListener)listener).enterSpecifications(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof TQLListener ) ((TQLListener)listener).exitSpecifications(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof TQLVisitor ) return ((TQLVisitor<? extends T>)visitor).visitSpecifications(this);
			else return visitor.visitChildren(this);
		}
	}

	public final SpecificationsContext specifications() throws RecognitionException {
		SpecificationsContext _localctx = new SpecificationsContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_specifications);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(61);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__0) {
				{
				setState(60);
				attributes();
				}
			}

			setState(66);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==WITH) {
				{
				setState(63);
				match(WITH);
				setState(64);
				match(INTEGER);
				setState(65);
				match(PARTICIPANT);
				}
			}

			setState(69);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__6) {
				{
				setState(68);
				list();
				}
			}

			setState(73);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==CONTENDER) {
				{
				setState(71);
				match(CONTENDER);
				setState(72);
				_la = _input.LA(1);
				if ( !(_la==TEAM || _la==PLAYER) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				}
			}

			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class AttributesContext extends ParserRuleContext {
		public List<TerminalNode> WORD() { return getTokens(TQLParser.WORD); }
		public TerminalNode WORD(int i) {
			return getToken(TQLParser.WORD, i);
		}
		public AttributesContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_attributes; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof TQLListener ) ((TQLListener)listener).enterAttributes(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof TQLListener ) ((TQLListener)listener).exitAttributes(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof TQLVisitor ) return ((TQLVisitor<? extends T>)visitor).visitAttributes(this);
			else return visitor.visitChildren(this);
		}
	}

	public final AttributesContext attributes() throws RecognitionException {
		AttributesContext _localctx = new AttributesContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_attributes);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(75);
			match(T__0);
			setState(76);
			match(WORD);
			setState(81);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==T__1) {
				{
				{
				setState(77);
				match(T__1);
				setState(78);
				match(WORD);
				}
				}
				setState(83);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(84);
			match(T__2);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Add_queryContext extends ParserRuleContext {
		public TerminalNode ADD() { return getToken(TQLParser.ADD, 0); }
		public TerminalNode PARTICIPANT() { return getToken(TQLParser.PARTICIPANT, 0); }
		public TerminalNode TO() { return getToken(TQLParser.TO, 0); }
		public T_identifierContext t_identifier() {
			return getRuleContext(T_identifierContext.class,0);
		}
		public NameContext name() {
			return getRuleContext(NameContext.class,0);
		}
		public ListContext list() {
			return getRuleContext(ListContext.class,0);
		}
		public Add_queryContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_add_query; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof TQLListener ) ((TQLListener)listener).enterAdd_query(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof TQLListener ) ((TQLListener)listener).exitAdd_query(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof TQLVisitor ) return ((TQLVisitor<? extends T>)visitor).visitAdd_query(this);
			else return visitor.visitChildren(this);
		}
	}

	public final Add_queryContext add_query() throws RecognitionException {
		Add_queryContext _localctx = new Add_queryContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_add_query);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(86);
			match(ADD);
			setState(87);
			match(PARTICIPANT);
			setState(88);
			match(TO);
			setState(89);
			t_identifier();
			setState(92);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case STRING:
				{
				setState(90);
				name();
				}
				break;
			case T__6:
				{
				setState(91);
				list();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Delete_queryContext extends ParserRuleContext {
		public TerminalNode DELETE() { return getToken(TQLParser.DELETE, 0); }
		public TerminalNode FROM() { return getToken(TQLParser.FROM, 0); }
		public T_identifierContext t_identifier() {
			return getRuleContext(T_identifierContext.class,0);
		}
		public TerminalNode WORD() { return getToken(TQLParser.WORD, 0); }
		public AttributesContext attributes() {
			return getRuleContext(AttributesContext.class,0);
		}
		public ListContext list() {
			return getRuleContext(ListContext.class,0);
		}
		public Delete_queryContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_delete_query; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof TQLListener ) ((TQLListener)listener).enterDelete_query(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof TQLListener ) ((TQLListener)listener).exitDelete_query(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof TQLVisitor ) return ((TQLVisitor<? extends T>)visitor).visitDelete_query(this);
			else return visitor.visitChildren(this);
		}
	}

	public final Delete_queryContext delete_query() throws RecognitionException {
		Delete_queryContext _localctx = new Delete_queryContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_delete_query);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(94);
			match(DELETE);
			setState(98);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case WORD:
				{
				setState(95);
				match(WORD);
				}
				break;
			case T__0:
				{
				setState(96);
				attributes();
				}
				break;
			case T__6:
				{
				setState(97);
				list();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
			setState(100);
			match(FROM);
			setState(101);
			t_identifier();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Modify_queryContext extends ParserRuleContext {
		public TerminalNode MODIFY() { return getToken(TQLParser.MODIFY, 0); }
		public TerminalNode PARTICIPANT() { return getToken(TQLParser.PARTICIPANT, 0); }
		public TerminalNode FROM() { return getToken(TQLParser.FROM, 0); }
		public T_identifierContext t_identifier() {
			return getRuleContext(T_identifierContext.class,0);
		}
		public List<PairContext> pair() {
			return getRuleContexts(PairContext.class);
		}
		public PairContext pair(int i) {
			return getRuleContext(PairContext.class,i);
		}
		public TerminalNode WORD() { return getToken(TQLParser.WORD, 0); }
		public TerminalNode INTEGER() { return getToken(TQLParser.INTEGER, 0); }
		public Modify_queryContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_modify_query; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof TQLListener ) ((TQLListener)listener).enterModify_query(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof TQLListener ) ((TQLListener)listener).exitModify_query(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof TQLVisitor ) return ((TQLVisitor<? extends T>)visitor).visitModify_query(this);
			else return visitor.visitChildren(this);
		}
	}

	public final Modify_queryContext modify_query() throws RecognitionException {
		Modify_queryContext _localctx = new Modify_queryContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_modify_query);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(103);
			match(MODIFY);
			setState(104);
			match(PARTICIPANT);
			setState(105);
			_la = _input.LA(1);
			if ( !(_la==WORD || _la==INTEGER) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			setState(106);
			match(FROM);
			setState(107);
			t_identifier();
			setState(108);
			match(T__3);
			setState(109);
			pair();
			setState(114);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==T__1) {
				{
				{
				setState(110);
				match(T__1);
				setState(111);
				pair();
				}
				}
				setState(116);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(117);
			match(T__4);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Organize_queryContext extends ParserRuleContext {
		public TerminalNode ORGANIZE() { return getToken(TQLParser.ORGANIZE, 0); }
		public TerminalNode TOURNAMENT() { return getToken(TQLParser.TOURNAMENT, 0); }
		public T_identifierContext t_identifier() {
			return getRuleContext(T_identifierContext.class,0);
		}
		public TerminalNode BY() { return getToken(TQLParser.BY, 0); }
		public TerminalNode WORD() { return getToken(TQLParser.WORD, 0); }
		public Organize_queryContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_organize_query; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof TQLListener ) ((TQLListener)listener).enterOrganize_query(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof TQLListener ) ((TQLListener)listener).exitOrganize_query(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof TQLVisitor ) return ((TQLVisitor<? extends T>)visitor).visitOrganize_query(this);
			else return visitor.visitChildren(this);
		}
	}

	public final Organize_queryContext organize_query() throws RecognitionException {
		Organize_queryContext _localctx = new Organize_queryContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_organize_query);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(119);
			match(ORGANIZE);
			setState(120);
			match(TOURNAMENT);
			setState(121);
			t_identifier();
			setState(122);
			match(BY);
			setState(123);
			match(WORD);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Report_queryContext extends ParserRuleContext {
		public TerminalNode REPORT() { return getToken(TQLParser.REPORT, 0); }
		public A_identifierContext a_identifier() {
			return getRuleContext(A_identifierContext.class,0);
		}
		public TerminalNode OF() { return getToken(TQLParser.OF, 0); }
		public P_identifierContext p_identifier() {
			return getRuleContext(P_identifierContext.class,0);
		}
		public TerminalNode FROM() { return getToken(TQLParser.FROM, 0); }
		public T_identifierContext t_identifier() {
			return getRuleContext(T_identifierContext.class,0);
		}
		public Report_queryContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_report_query; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof TQLListener ) ((TQLListener)listener).enterReport_query(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof TQLListener ) ((TQLListener)listener).exitReport_query(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof TQLVisitor ) return ((TQLVisitor<? extends T>)visitor).visitReport_query(this);
			else return visitor.visitChildren(this);
		}
	}

	public final Report_queryContext report_query() throws RecognitionException {
		Report_queryContext _localctx = new Report_queryContext(_ctx, getState());
		enterRule(_localctx, 18, RULE_report_query);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(125);
			match(REPORT);
			setState(126);
			a_identifier();
			setState(127);
			match(OF);
			setState(128);
			p_identifier();
			setState(129);
			match(FROM);
			setState(130);
			t_identifier();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Show_queryContext extends ParserRuleContext {
		public TerminalNode SHOW() { return getToken(TQLParser.SHOW, 0); }
		public TerminalNode FROM() { return getToken(TQLParser.FROM, 0); }
		public T_identifierContext t_identifier() {
			return getRuleContext(T_identifierContext.class,0);
		}
		public TerminalNode PHASE() { return getToken(TQLParser.PHASE, 0); }
		public TerminalNode SUMMARY() { return getToken(TQLParser.SUMMARY, 0); }
		public TerminalNode OF() { return getToken(TQLParser.OF, 0); }
		public P_identifierContext p_identifier() {
			return getRuleContext(P_identifierContext.class,0);
		}
		public Show_queryContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_show_query; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof TQLListener ) ((TQLListener)listener).enterShow_query(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof TQLListener ) ((TQLListener)listener).exitShow_query(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof TQLVisitor ) return ((TQLVisitor<? extends T>)visitor).visitShow_query(this);
			else return visitor.visitChildren(this);
		}
	}

	public final Show_queryContext show_query() throws RecognitionException {
		Show_queryContext _localctx = new Show_queryContext(_ctx, getState());
		enterRule(_localctx, 20, RULE_show_query);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(132);
			match(SHOW);
			setState(133);
			_la = _input.LA(1);
			if ( !(_la==PHASE || _la==SUMMARY) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			setState(136);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==OF) {
				{
				setState(134);
				match(OF);
				setState(135);
				p_identifier();
				}
			}

			setState(138);
			match(FROM);
			setState(139);
			t_identifier();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class DtypeContext extends ParserRuleContext {
		public TerminalNode WORD() { return getToken(TQLParser.WORD, 0); }
		public TerminalNode INTEGER() { return getToken(TQLParser.INTEGER, 0); }
		public ListContext list() {
			return getRuleContext(ListContext.class,0);
		}
		public DtypeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_dtype; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof TQLListener ) ((TQLListener)listener).enterDtype(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof TQLListener ) ((TQLListener)listener).exitDtype(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof TQLVisitor ) return ((TQLVisitor<? extends T>)visitor).visitDtype(this);
			else return visitor.visitChildren(this);
		}
	}

	public final DtypeContext dtype() throws RecognitionException {
		DtypeContext _localctx = new DtypeContext(_ctx, getState());
		enterRule(_localctx, 22, RULE_dtype);
		try {
			setState(144);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case WORD:
				enterOuterAlt(_localctx, 1);
				{
				setState(141);
				match(WORD);
				}
				break;
			case INTEGER:
				enterOuterAlt(_localctx, 2);
				{
				setState(142);
				match(INTEGER);
				}
				break;
			case T__6:
				enterOuterAlt(_localctx, 3);
				{
				setState(143);
				list();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class PairContext extends ParserRuleContext {
		public TerminalNode WORD() { return getToken(TQLParser.WORD, 0); }
		public DtypeContext dtype() {
			return getRuleContext(DtypeContext.class,0);
		}
		public PairContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_pair; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof TQLListener ) ((TQLListener)listener).enterPair(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof TQLListener ) ((TQLListener)listener).exitPair(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof TQLVisitor ) return ((TQLVisitor<? extends T>)visitor).visitPair(this);
			else return visitor.visitChildren(this);
		}
	}

	public final PairContext pair() throws RecognitionException {
		PairContext _localctx = new PairContext(_ctx, getState());
		enterRule(_localctx, 24, RULE_pair);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(146);
			match(WORD);
			setState(147);
			match(T__5);
			setState(148);
			dtype();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ListContext extends ParserRuleContext {
		public List<NameContext> name() {
			return getRuleContexts(NameContext.class);
		}
		public NameContext name(int i) {
			return getRuleContext(NameContext.class,i);
		}
		public ListContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_list; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof TQLListener ) ((TQLListener)listener).enterList(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof TQLListener ) ((TQLListener)listener).exitList(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof TQLVisitor ) return ((TQLVisitor<? extends T>)visitor).visitList(this);
			else return visitor.visitChildren(this);
		}
	}

	public final ListContext list() throws RecognitionException {
		ListContext _localctx = new ListContext(_ctx, getState());
		enterRule(_localctx, 26, RULE_list);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(150);
			match(T__6);
			setState(151);
			name();
			setState(156);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==T__1) {
				{
				{
				setState(152);
				match(T__1);
				setState(153);
				name();
				}
				}
				setState(158);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(159);
			match(T__7);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class A_identifierContext extends ParserRuleContext {
		public TerminalNode WORD() { return getToken(TQLParser.WORD, 0); }
		public A_identifierContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_a_identifier; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof TQLListener ) ((TQLListener)listener).enterA_identifier(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof TQLListener ) ((TQLListener)listener).exitA_identifier(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof TQLVisitor ) return ((TQLVisitor<? extends T>)visitor).visitA_identifier(this);
			else return visitor.visitChildren(this);
		}
	}

	public final A_identifierContext a_identifier() throws RecognitionException {
		A_identifierContext _localctx = new A_identifierContext(_ctx, getState());
		enterRule(_localctx, 28, RULE_a_identifier);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(161);
			match(WORD);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class T_identifierContext extends ParserRuleContext {
		public TerminalNode STRING() { return getToken(TQLParser.STRING, 0); }
		public TerminalNode WORD() { return getToken(TQLParser.WORD, 0); }
		public T_identifierContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_t_identifier; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof TQLListener ) ((TQLListener)listener).enterT_identifier(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof TQLListener ) ((TQLListener)listener).exitT_identifier(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof TQLVisitor ) return ((TQLVisitor<? extends T>)visitor).visitT_identifier(this);
			else return visitor.visitChildren(this);
		}
	}

	public final T_identifierContext t_identifier() throws RecognitionException {
		T_identifierContext _localctx = new T_identifierContext(_ctx, getState());
		enterRule(_localctx, 30, RULE_t_identifier);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(163);
			_la = _input.LA(1);
			if ( !(_la==STRING || _la==WORD) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class P_identifierContext extends ParserRuleContext {
		public TerminalNode STRING() { return getToken(TQLParser.STRING, 0); }
		public TerminalNode WORD() { return getToken(TQLParser.WORD, 0); }
		public P_identifierContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_p_identifier; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof TQLListener ) ((TQLListener)listener).enterP_identifier(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof TQLListener ) ((TQLListener)listener).exitP_identifier(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof TQLVisitor ) return ((TQLVisitor<? extends T>)visitor).visitP_identifier(this);
			else return visitor.visitChildren(this);
		}
	}

	public final P_identifierContext p_identifier() throws RecognitionException {
		P_identifierContext _localctx = new P_identifierContext(_ctx, getState());
		enterRule(_localctx, 32, RULE_p_identifier);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(165);
			_la = _input.LA(1);
			if ( !(_la==STRING || _la==WORD) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class IdentifierContext extends ParserRuleContext {
		public TerminalNode WORD() { return getToken(TQLParser.WORD, 0); }
		public IdentifierContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_identifier; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof TQLListener ) ((TQLListener)listener).enterIdentifier(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof TQLListener ) ((TQLListener)listener).exitIdentifier(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof TQLVisitor ) return ((TQLVisitor<? extends T>)visitor).visitIdentifier(this);
			else return visitor.visitChildren(this);
		}
	}

	public final IdentifierContext identifier() throws RecognitionException {
		IdentifierContext _localctx = new IdentifierContext(_ctx, getState());
		enterRule(_localctx, 34, RULE_identifier);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(167);
			match(WORD);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class NameContext extends ParserRuleContext {
		public TerminalNode STRING() { return getToken(TQLParser.STRING, 0); }
		public AbbrContext abbr() {
			return getRuleContext(AbbrContext.class,0);
		}
		public NameContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_name; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof TQLListener ) ((TQLListener)listener).enterName(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof TQLListener ) ((TQLListener)listener).exitName(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof TQLVisitor ) return ((TQLVisitor<? extends T>)visitor).visitName(this);
			else return visitor.visitChildren(this);
		}
	}

	public final NameContext name() throws RecognitionException {
		NameContext _localctx = new NameContext(_ctx, getState());
		enterRule(_localctx, 36, RULE_name);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(169);
			match(STRING);
			setState(174);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,14,_ctx) ) {
			case 1:
				{
				setState(170);
				match(T__0);
				setState(171);
				abbr();
				setState(172);
				match(T__2);
				}
				break;
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class AbbrContext extends ParserRuleContext {
		public TerminalNode WORD() { return getToken(TQLParser.WORD, 0); }
		public AbbrContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_abbr; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof TQLListener ) ((TQLListener)listener).enterAbbr(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof TQLListener ) ((TQLListener)listener).exitAbbr(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof TQLVisitor ) return ((TQLVisitor<? extends T>)visitor).visitAbbr(this);
			else return visitor.visitChildren(this);
		}
	}

	public final AbbrContext abbr() throws RecognitionException {
		AbbrContext _localctx = new AbbrContext(_ctx, getState());
		enterRule(_localctx, 38, RULE_abbr);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(176);
			match(WORD);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static final String _serializedATN =
		"\u0004\u0001\"\u00b3\u0002\u0000\u0007\u0000\u0002\u0001\u0007\u0001\u0002"+
		"\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004\u0007\u0004\u0002"+
		"\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002\u0007\u0007\u0007\u0002"+
		"\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0002\u000b\u0007\u000b\u0002"+
		"\f\u0007\f\u0002\r\u0007\r\u0002\u000e\u0007\u000e\u0002\u000f\u0007\u000f"+
		"\u0002\u0010\u0007\u0010\u0002\u0011\u0007\u0011\u0002\u0012\u0007\u0012"+
		"\u0002\u0013\u0007\u0013\u0001\u0000\u0004\u0000*\b\u0000\u000b\u0000"+
		"\f\u0000+\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001"+
		"\u0001\u0001\u0001\u0001\u0003\u00015\b\u0001\u0001\u0002\u0001\u0002"+
		"\u0001\u0002\u0001\u0002\u0003\u0002;\b\u0002\u0001\u0003\u0003\u0003"+
		">\b\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0003\u0003C\b\u0003\u0001"+
		"\u0003\u0003\u0003F\b\u0003\u0001\u0003\u0001\u0003\u0003\u0003J\b\u0003"+
		"\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0005\u0004P\b\u0004"+
		"\n\u0004\f\u0004S\t\u0004\u0001\u0004\u0001\u0004\u0001\u0005\u0001\u0005"+
		"\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0003\u0005]\b\u0005"+
		"\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0003\u0006c\b\u0006"+
		"\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0007\u0001\u0007\u0001\u0007"+
		"\u0001\u0007\u0001\u0007\u0001\u0007\u0001\u0007\u0001\u0007\u0001\u0007"+
		"\u0005\u0007q\b\u0007\n\u0007\f\u0007t\t\u0007\u0001\u0007\u0001\u0007"+
		"\u0001\b\u0001\b\u0001\b\u0001\b\u0001\b\u0001\b\u0001\t\u0001\t\u0001"+
		"\t\u0001\t\u0001\t\u0001\t\u0001\t\u0001\n\u0001\n\u0001\n\u0001\n\u0003"+
		"\n\u0089\b\n\u0001\n\u0001\n\u0001\n\u0001\u000b\u0001\u000b\u0001\u000b"+
		"\u0003\u000b\u0091\b\u000b\u0001\f\u0001\f\u0001\f\u0001\f\u0001\r\u0001"+
		"\r\u0001\r\u0001\r\u0005\r\u009b\b\r\n\r\f\r\u009e\t\r\u0001\r\u0001\r"+
		"\u0001\u000e\u0001\u000e\u0001\u000f\u0001\u000f\u0001\u0010\u0001\u0010"+
		"\u0001\u0011\u0001\u0011\u0001\u0012\u0001\u0012\u0001\u0012\u0001\u0012"+
		"\u0001\u0012\u0003\u0012\u00af\b\u0012\u0001\u0013\u0001\u0013\u0001\u0013"+
		"\u0000\u0000\u0014\u0000\u0002\u0004\u0006\b\n\f\u000e\u0010\u0012\u0014"+
		"\u0016\u0018\u001a\u001c\u001e \"$&\u0000\u0004\u0001\u0000\u001c\u001d"+
		"\u0001\u0000 !\u0001\u0000\u001a\u001b\u0001\u0000\u001f \u00b4\u0000"+
		")\u0001\u0000\u0000\u0000\u00024\u0001\u0000\u0000\u0000\u00046\u0001"+
		"\u0000\u0000\u0000\u0006=\u0001\u0000\u0000\u0000\bK\u0001\u0000\u0000"+
		"\u0000\nV\u0001\u0000\u0000\u0000\f^\u0001\u0000\u0000\u0000\u000eg\u0001"+
		"\u0000\u0000\u0000\u0010w\u0001\u0000\u0000\u0000\u0012}\u0001\u0000\u0000"+
		"\u0000\u0014\u0084\u0001\u0000\u0000\u0000\u0016\u0090\u0001\u0000\u0000"+
		"\u0000\u0018\u0092\u0001\u0000\u0000\u0000\u001a\u0096\u0001\u0000\u0000"+
		"\u0000\u001c\u00a1\u0001\u0000\u0000\u0000\u001e\u00a3\u0001\u0000\u0000"+
		"\u0000 \u00a5\u0001\u0000\u0000\u0000\"\u00a7\u0001\u0000\u0000\u0000"+
		"$\u00a9\u0001\u0000\u0000\u0000&\u00b0\u0001\u0000\u0000\u0000(*\u0003"+
		"\u0002\u0001\u0000)(\u0001\u0000\u0000\u0000*+\u0001\u0000\u0000\u0000"+
		"+)\u0001\u0000\u0000\u0000+,\u0001\u0000\u0000\u0000,\u0001\u0001\u0000"+
		"\u0000\u0000-5\u0003\u0004\u0002\u0000.5\u0003\n\u0005\u0000/5\u0003\f"+
		"\u0006\u000005\u0003\u000e\u0007\u000015\u0003\u0010\b\u000025\u0003\u0012"+
		"\t\u000035\u0003\u0014\n\u00004-\u0001\u0000\u0000\u00004.\u0001\u0000"+
		"\u0000\u00004/\u0001\u0000\u0000\u000040\u0001\u0000\u0000\u000041\u0001"+
		"\u0000\u0000\u000042\u0001\u0000\u0000\u000043\u0001\u0000\u0000\u0000"+
		"5\u0003\u0001\u0000\u0000\u000067\u0005\t\u0000\u000078\u0005\n\u0000"+
		"\u00008:\u0003$\u0012\u00009;\u0003\u0006\u0003\u0000:9\u0001\u0000\u0000"+
		"\u0000:;\u0001\u0000\u0000\u0000;\u0005\u0001\u0000\u0000\u0000<>\u0003"+
		"\b\u0004\u0000=<\u0001\u0000\u0000\u0000=>\u0001\u0000\u0000\u0000>B\u0001"+
		"\u0000\u0000\u0000?@\u0005\u000b\u0000\u0000@A\u0005!\u0000\u0000AC\u0005"+
		"\f\u0000\u0000B?\u0001\u0000\u0000\u0000BC\u0001\u0000\u0000\u0000CE\u0001"+
		"\u0000\u0000\u0000DF\u0003\u001a\r\u0000ED\u0001\u0000\u0000\u0000EF\u0001"+
		"\u0000\u0000\u0000FI\u0001\u0000\u0000\u0000GH\u0005\u001e\u0000\u0000"+
		"HJ\u0007\u0000\u0000\u0000IG\u0001\u0000\u0000\u0000IJ\u0001\u0000\u0000"+
		"\u0000J\u0007\u0001\u0000\u0000\u0000KL\u0005\u0001\u0000\u0000LQ\u0005"+
		" \u0000\u0000MN\u0005\u0002\u0000\u0000NP\u0005 \u0000\u0000OM\u0001\u0000"+
		"\u0000\u0000PS\u0001\u0000\u0000\u0000QO\u0001\u0000\u0000\u0000QR\u0001"+
		"\u0000\u0000\u0000RT\u0001\u0000\u0000\u0000SQ\u0001\u0000\u0000\u0000"+
		"TU\u0005\u0003\u0000\u0000U\t\u0001\u0000\u0000\u0000VW\u0005\r\u0000"+
		"\u0000WX\u0005\f\u0000\u0000XY\u0005\u000e\u0000\u0000Y\\\u0003\u001e"+
		"\u000f\u0000Z]\u0003$\u0012\u0000[]\u0003\u001a\r\u0000\\Z\u0001\u0000"+
		"\u0000\u0000\\[\u0001\u0000\u0000\u0000]\u000b\u0001\u0000\u0000\u0000"+
		"^b\u0005\u0011\u0000\u0000_c\u0005 \u0000\u0000`c\u0003\b\u0004\u0000"+
		"ac\u0003\u001a\r\u0000b_\u0001\u0000\u0000\u0000b`\u0001\u0000\u0000\u0000"+
		"ba\u0001\u0000\u0000\u0000cd\u0001\u0000\u0000\u0000de\u0005\u0012\u0000"+
		"\u0000ef\u0003\u001e\u000f\u0000f\r\u0001\u0000\u0000\u0000gh\u0005\u0015"+
		"\u0000\u0000hi\u0005\f\u0000\u0000ij\u0007\u0001\u0000\u0000jk\u0005\u0012"+
		"\u0000\u0000kl\u0003\u001e\u000f\u0000lm\u0005\u0004\u0000\u0000mr\u0003"+
		"\u0018\f\u0000no\u0005\u0002\u0000\u0000oq\u0003\u0018\f\u0000pn\u0001"+
		"\u0000\u0000\u0000qt\u0001\u0000\u0000\u0000rp\u0001\u0000\u0000\u0000"+
		"rs\u0001\u0000\u0000\u0000su\u0001\u0000\u0000\u0000tr\u0001\u0000\u0000"+
		"\u0000uv\u0005\u0005\u0000\u0000v\u000f\u0001\u0000\u0000\u0000wx\u0005"+
		"\u000f\u0000\u0000xy\u0005\n\u0000\u0000yz\u0003\u001e\u000f\u0000z{\u0005"+
		"\u0013\u0000\u0000{|\u0005 \u0000\u0000|\u0011\u0001\u0000\u0000\u0000"+
		"}~\u0005\u0014\u0000\u0000~\u007f\u0003\u001c\u000e\u0000\u007f\u0080"+
		"\u0005\u0017\u0000\u0000\u0080\u0081\u0003 \u0010\u0000\u0081\u0082\u0005"+
		"\u0012\u0000\u0000\u0082\u0083\u0003\u001e\u000f\u0000\u0083\u0013\u0001"+
		"\u0000\u0000\u0000\u0084\u0085\u0005\u0019\u0000\u0000\u0085\u0088\u0007"+
		"\u0002\u0000\u0000\u0086\u0087\u0005\u0017\u0000\u0000\u0087\u0089\u0003"+
		" \u0010\u0000\u0088\u0086\u0001\u0000\u0000\u0000\u0088\u0089\u0001\u0000"+
		"\u0000\u0000\u0089\u008a\u0001\u0000\u0000\u0000\u008a\u008b\u0005\u0012"+
		"\u0000\u0000\u008b\u008c\u0003\u001e\u000f\u0000\u008c\u0015\u0001\u0000"+
		"\u0000\u0000\u008d\u0091\u0005 \u0000\u0000\u008e\u0091\u0005!\u0000\u0000"+
		"\u008f\u0091\u0003\u001a\r\u0000\u0090\u008d\u0001\u0000\u0000\u0000\u0090"+
		"\u008e\u0001\u0000\u0000\u0000\u0090\u008f\u0001\u0000\u0000\u0000\u0091"+
		"\u0017\u0001\u0000\u0000\u0000\u0092\u0093\u0005 \u0000\u0000\u0093\u0094"+
		"\u0005\u0006\u0000\u0000\u0094\u0095\u0003\u0016\u000b\u0000\u0095\u0019"+
		"\u0001\u0000\u0000\u0000\u0096\u0097\u0005\u0007\u0000\u0000\u0097\u009c"+
		"\u0003$\u0012\u0000\u0098\u0099\u0005\u0002\u0000\u0000\u0099\u009b\u0003"+
		"$\u0012\u0000\u009a\u0098\u0001\u0000\u0000\u0000\u009b\u009e\u0001\u0000"+
		"\u0000\u0000\u009c\u009a\u0001\u0000\u0000\u0000\u009c\u009d\u0001\u0000"+
		"\u0000\u0000\u009d\u009f\u0001\u0000\u0000\u0000\u009e\u009c\u0001\u0000"+
		"\u0000\u0000\u009f\u00a0\u0005\b\u0000\u0000\u00a0\u001b\u0001\u0000\u0000"+
		"\u0000\u00a1\u00a2\u0005 \u0000\u0000\u00a2\u001d\u0001\u0000\u0000\u0000"+
		"\u00a3\u00a4\u0007\u0003\u0000\u0000\u00a4\u001f\u0001\u0000\u0000\u0000"+
		"\u00a5\u00a6\u0007\u0003\u0000\u0000\u00a6!\u0001\u0000\u0000\u0000\u00a7"+
		"\u00a8\u0005 \u0000\u0000\u00a8#\u0001\u0000\u0000\u0000\u00a9\u00ae\u0005"+
		"\u001f\u0000\u0000\u00aa\u00ab\u0005\u0001\u0000\u0000\u00ab\u00ac\u0003"+
		"&\u0013\u0000\u00ac\u00ad\u0005\u0003\u0000\u0000\u00ad\u00af\u0001\u0000"+
		"\u0000\u0000\u00ae\u00aa\u0001\u0000\u0000\u0000\u00ae\u00af\u0001\u0000"+
		"\u0000\u0000\u00af%\u0001\u0000\u0000\u0000\u00b0\u00b1\u0005 \u0000\u0000"+
		"\u00b1\'\u0001\u0000\u0000\u0000\u000f+4:=BEIQ\\br\u0088\u0090\u009c\u00ae";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}