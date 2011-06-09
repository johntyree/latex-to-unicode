def convert(s):
	ss = convert_single_symbol(s)
	if ss != None:
		return ss

	s = convert_latex_symbols(s)
	s = convert_superscripts(s)
	s = convert_subscripts(s)
	return s

# If s is just a latex code "alpha" or "beta" it converts it to its
# unicode representation.
def convert_single_symbol(s):
	ss = "\\" + s
	if ss in latex_symbols:
		return latex_symbols[ss]
	return None

# Replace each "\alpha", "\beta" and similar latex symbols with
# their unicode representation.
def convert_latex_symbols(s):
	for key, val in latex_symbols.items():
		s = s.replace(key, val)
	return s

# _23 => ₂3
# _{23} => ₂₃
def convert_superscripts(s):
	s = list(s)
	ss = ""
	mode_normal, mode_caret, mode_long = range(3)
	mode = mode_normal
	for ch in s:
		if mode == mode_normal and ch == '^':
			mode = mode_caret
			continue
		elif mode == mode_caret and ch == '{':
			mode = mode_long
			continue
		elif mode == mode_caret:
			ss += translate_if_possible(ch, supscripts)
			mode = mode_normal
			continue
		elif mode == mode_long and ch == '}':
			mode = mode_normal
			continue

		if mode == mode_normal:
			ss += ch
		else:
			ss += translate_if_possible(ch, supscripts)
	return ss

# ^23 => ²3
# ^{23} => ²³
def convert_subscripts(s):
	s = list(s)
	ss = ""
	mode_normal, mode_caret, mode_long = range(3)
	mode = mode_normal
	for ch in s:
		if mode == mode_normal and ch == '_':
			mode = mode_caret
			continue
		elif mode == mode_caret and ch == '{':
			mode = mode_long
			continue
		elif mode == mode_caret:
			ss += translate_if_possible(ch, subscripts)
			mode = mode_normal
			continue
		elif mode == mode_long and ch == '}':
			mode = mode_normal
			continue

		if mode == mode_normal:
			ss += ch
		else:
			ss += translate_if_possible(ch, subscripts)
	return ss

def translate_if_possible(ch, d):
	if ch in d:
		return d[ch]
	return ch

supscripts = {}
supscripts["0"] = "⁰"
supscripts["1"] = "¹"
supscripts["2"] = "²"
supscripts["3"] = "³"
supscripts["4"] = "⁴"
supscripts["5"] = "⁵"
supscripts["6"] = "⁶"
supscripts["7"] = "⁷"
supscripts["8"] = "⁸"
supscripts["9"] = "⁹"
supscripts["+"] = "⁺"
supscripts["-"] = "⁻"
supscripts["="] = "⁼"

subscripts = {}
subscripts["0"] = "₀"
subscripts["1"] = "₁"
subscripts["2"] = "₂"
subscripts["3"] = "₃"
subscripts["4"] = "₄"
subscripts["5"] = "₅"
subscripts["6"] = "₆"
subscripts["7"] = "₇"
subscripts["8"] = "₈"
subscripts["9"] = "₉"
subscripts["+"] = "₊"
subscripts["-"] = "₋"
subscripts["="] = "₌"

latex_symbols = {}
latex_symbols["\\alpha"] = "α"
latex_symbols["\\beta"] = "β"
latex_symbols["\\gamma"] = "γ"
latex_symbols["\\delta"] = "δ"
latex_symbols["\\epsilon"] = "∊"
latex_symbols["\\varepsilon"] = "ε"
latex_symbols["\\zeta"] = "ζ"
latex_symbols["\\eta"] = "η"
latex_symbols["\\theta"] = "θ"
latex_symbols["\\vartheta"] = "ϑ"
latex_symbols["\\iota"] = "ι"
latex_symbols["\\kappa"] = "κ"
latex_symbols["\\lambda"] = "λ"
latex_symbols["\\mu"] = "μ"
latex_symbols["\\nu"] = "ν"
latex_symbols["\\xi"] = "ξ"
latex_symbols["\\pi"] = "π"
latex_symbols["\\varpi"] = "ϖ"
latex_symbols["\\rho"] = "ρ"
latex_symbols["\\varrho"] = "ϱ"
latex_symbols["\\sigma"] = "σ"
latex_symbols["\\varsigma"] = "ς"
latex_symbols["\\tau"] = "τ"
latex_symbols["\\upsilon"] = "υ"
latex_symbols["\\phi"] = "φ"
latex_symbols["\\varphi"] = "ϕ"
latex_symbols["\\chi"] = "χ"
latex_symbols["\\psi"] = "ψ"
latex_symbols["\\omega"] = "ω"
latex_symbols["\\Gamma"] = "Γ"
latex_symbols["\\Delta"] = "Δ"
latex_symbols["\\Theta"] = "Θ"
latex_symbols["\\Lambda"] = "Λ"
latex_symbols["\\Xi"] = "Ξ"
latex_symbols["\\Pi"] = "Π"
latex_symbols["\\Upsilon"] = "Υ"
latex_symbols["\\Phi"] = "Φ"
latex_symbols["\\Psi"] = "Ψ"
latex_symbols["\\Omega"] = "Ω"
latex_symbols["\\leq"] = "≤"
latex_symbols["\\ll"] = "≪"
latex_symbols["\\prec"] = "≺"
latex_symbols["\\preceq"] = "≼"
latex_symbols["\\subset"] = "⊂"
latex_symbols["\\subseteq"] = "⊆"
latex_symbols["\\sqsubset"] = "⊏"
latex_symbols["\\sqsubseteq"] = "⊑"
latex_symbols["\\in"] = "∈"
latex_symbols["\\vdash"] = "⊢"
latex_symbols["\\mid"] = "∣"
latex_symbols["\\smile"] = "⌣"
latex_symbols["\\geq"] = "≥"
latex_symbols["\\gg"] = "≫"
latex_symbols["\\succ"] = "≻"
latex_symbols["\\succeq"] = "≽"
latex_symbols["\\supset"] = "⊃"
latex_symbols["\\supseteq"] = "⊇"
latex_symbols["\\sqsupset"] = "⊐"
latex_symbols["\\sqsupseteq"] = "⊒"
latex_symbols["\\ni"] = "∋"
latex_symbols["\\dashv"] = "⊣"
latex_symbols["\\parallel"] = "∥"
latex_symbols["\\frown"] = "⌢"
latex_symbols["\\notin"] = "∉"
latex_symbols["\\equiv"] = "≡"
latex_symbols["\\doteq"] = "≐"
latex_symbols["\\sim"] = "∼"
latex_symbols["\\simeq"] = "≃"
latex_symbols["\\approx"] = "≈"
latex_symbols["\\cong"] = "≅"
latex_symbols["\\Join"] = "⋈"
latex_symbols["\\bowtie"] = "⋈"
latex_symbols["\\propto"] = "∝"
latex_symbols["\\models"] = "⊨"
latex_symbols["\\perp"] = "⊥"
latex_symbols["\\asymp"] = "≍"
latex_symbols["\\neq"] = "≠"
latex_symbols["\\pm"] = "±"
latex_symbols["\\cdot"] = "⋅"
latex_symbols["\\times"] = "×"
latex_symbols["\\cup"] = "∪"
latex_symbols["\\sqcup"] = "⊔"
latex_symbols["\\vee"] = "∨"
latex_symbols["\\oplus"] = "⊕"
latex_symbols["\\odot"] = "⊙"
latex_symbols["\\otimes"] = "⊗"
latex_symbols["\\bigtriangleup"] = "△"
latex_symbols["\\lhd"] = "⊲"
latex_symbols["\\unlhd"] = "⊴"
latex_symbols["\\mp"] = "∓"
latex_symbols["\\div"] = "÷"
latex_symbols["\\setminus"] = "∖"
latex_symbols["\\cap"] = "∩"
latex_symbols["\\sqcap"] = "⊓"
latex_symbols["\\wedge"] = "∧"
latex_symbols["\\ominus"] = "⊖"
latex_symbols["\\oslash"] = "⊘"
latex_symbols["\\bigcirc"] = "○"
latex_symbols["\\bigtriangledown"] = "▽"
latex_symbols["\\rhd"] = "⊳"
latex_symbols["\\unrhd"] = "⊵"
latex_symbols["\\triangleleft"] = "◁"
latex_symbols["\\triangleright"] = "▷"
latex_symbols["\\star"] = "⋆"
latex_symbols["\\ast"] = "∗"
latex_symbols["\\circ"] = "∘"
latex_symbols["\\bullet"] = "∙"
latex_symbols["\\diamond"] = "⋄"
latex_symbols["\\uplus"] = "⊎"
latex_symbols["\\dagger"] = "†"
latex_symbols["\\ddagger"] = "‡"
latex_symbols["\\wr"] = "≀"
latex_symbols["\\sum"] = "∑"
latex_symbols["\\prod"] = "∏"
latex_symbols["\\coprod"] = "∐"
latex_symbols["\\int"] = "∫"
latex_symbols["\\bigcup"] = "⋃"
latex_symbols["\\bigcap"] = "⋂"
latex_symbols["\\bigsqcup"] = "⊔"
latex_symbols["\\oint"] = "∮"
latex_symbols["\\bigvee"] = "⋁"
latex_symbols["\\bigwedge"] = "⋀"
latex_symbols["\\bigoplus"] = "⊕"
latex_symbols["\\bigotimes"] = "⊗"
latex_symbols["\\bigodot"] = "⊙"
latex_symbols["\\biguplus"] = "⊎"
latex_symbols["\\leftarrow"] = "←"
latex_symbols["\\rightarrow"] = "→"
latex_symbols["\\leftrightarrow"] = "↔"
latex_symbols["\\Leftarrow"] = "⇐"
latex_symbols["\\Rightarrow"] = "⇒"
latex_symbols["\\Leftrightarrow"] = "⇔"
latex_symbols["\\mapsto"] = "↦"
latex_symbols["\\hookleftarrow"] = "↩"
latex_symbols["\\leftharpoonup"] = "↼"
latex_symbols["\\leftharpoondown"] = "↽"
latex_symbols["\\hookrightarrow"] = "↪"
latex_symbols["\\rightharpoonup"] = "⇀"
latex_symbols["\\rightharpoondown"] = "⇁"
latex_symbols["\\longleftarrow"] = "←"
latex_symbols["\\longrightarrow"] = "→"
latex_symbols["\\longleftrightarrow"] = "↔"
latex_symbols["\\Longleftarrow"] = "⇐"
latex_symbols["\\Longrightarrow"] = "⇒"
latex_symbols["\\Longleftrightarrow"] = "⇔"
latex_symbols["\\longmapsto"] = "⇖"
latex_symbols["\\uparrow"] = "↑"
latex_symbols["\\downarrow"] = "↓"
latex_symbols["\\updownarrow"] = "↕"
latex_symbols["\\Uparrow"] = "⇑"
latex_symbols["\\Downarrow"] = "⇓"
latex_symbols["\\Updownarrow"] = "⇕"
latex_symbols["\\nearrow"] = "↗"
latex_symbols["\\searrow"] = "↘"
latex_symbols["\\swarrow"] = "↙"
latex_symbols["\\nwarrow"] = "↖"
latex_symbols["\\leadsto"] = "↝"
latex_symbols["\\dots"] = "…"
latex_symbols["\\cdots"] = "⋯"
latex_symbols["\\vdots"] = "⋮"
latex_symbols["\\ddots"] = "⋱"
latex_symbols["\\hbar"] = "ℏ"
latex_symbols["\\ell"] = "ℓ"
latex_symbols["\\Re"] = "ℜ"
latex_symbols["\\Im"] = "ℑ"
latex_symbols["\\aleph"] = "א"
latex_symbols["\\wp"] = "℘"
latex_symbols["\\forall"] = "∀"
latex_symbols["\\exists"] = "∃"
latex_symbols["\\mho"] = "℧"
latex_symbols["\\partial"] = "∂"
latex_symbols["\\prime"] = "′"
latex_symbols["\\emptyset"] = "∅"
latex_symbols["\\infty"] = "∞"
latex_symbols["\\nabla"] = "∇"
latex_symbols["\\triangle"] = "△"
latex_symbols["\\Box"] = "□"
latex_symbols["\\Diamond"] = "◇"
latex_symbols["\\bot"] = "⊥"
latex_symbols["\\top"] = "⊤"
latex_symbols["\\angle"] = "∠"
latex_symbols["\\surd"] = "√"
latex_symbols["\\diamondsuit"] = "♢"
latex_symbols["\\heartsuit"] = "♡"
latex_symbols["\\clubsuit"] = "♣"
latex_symbols["\\spadesuit"] = "♠"
latex_symbols["\\neg"] = "¬"
latex_symbols["\\flat"] = "♭"
latex_symbols["\\natural"] = "♮"
latex_symbols["\\sharp"] = "♯"
latex_symbols["\\digamma"] = "Ϝ"
latex_symbols["\\varkappa"] = "ϰ"
latex_symbols["\\beth"] = "ב"
latex_symbols["\\daleth"] = "ד"
latex_symbols["\\gimel"] = "ג"
latex_symbols["\\lessdot"] = "⋖"
latex_symbols["\\leqslant"] = "≤"
latex_symbols["\\leqq"] = "≦"
latex_symbols["\\lll"] = "⋘"
latex_symbols["\\lesssim"] = "≲"
latex_symbols["\\lessgtr"] = "≶"
latex_symbols["\\lesseqgtr"] = "⋚"
latex_symbols["\\preccurlyeq"] = "≼"
latex_symbols["\\curlyeqprec"] = "⋞"
latex_symbols["\\precsim"] = "≾"
latex_symbols["\\Subset"] = "⋐"
latex_symbols["\\sqsubset"] = "⊏"
latex_symbols["\\therefore"] = "∴"
latex_symbols["\\smallsmile"] = "⌣"
latex_symbols["\\vartriangleleft"] = "⊲"
latex_symbols["\\trianglelefteq"] = "⊴"
latex_symbols["\\gtrdot"] = "⋗"
latex_symbols["\\geqq"] = "≧"
latex_symbols["\\ggg"] = "⋙"
latex_symbols["\\gtrsim"] = "≳"
latex_symbols["\\gtrless"] = "≷"
latex_symbols["\\gtreqless"] = "⋛"
latex_symbols["\\succcurlyeq"] = "≽"
latex_symbols["\\curlyeqsucc"] = "⋟"
latex_symbols["\\succsim"] = "≿"
latex_symbols["\\Supset"] = "⋑"
latex_symbols["\\sqsupset"] = "⊐"
latex_symbols["\\because"] = "∵"
latex_symbols["\\shortparallel"] = "∥"
latex_symbols["\\smallfrown"] = "⌢"
latex_symbols["\\vartriangleright"] = "⊳"
latex_symbols["\\trianglerighteq"] = "⊵"
latex_symbols["\\doteqdot"] = "≑"
latex_symbols["\\risingdotseq"] = "≓"
latex_symbols["\\fallingdotseq"] = "≒"
latex_symbols["\\eqcirc"] = "≖"
latex_symbols["\\circeq"] = "≗"
latex_symbols["\\triangleq"] = "≜"
latex_symbols["\\bumpeq"] = "≏"
latex_symbols["\\Bumpeq"] = "≎"
latex_symbols["\\thicksim"] = "∼"
latex_symbols["\\thickapprox"] = "≈"
latex_symbols["\\approxeq"] = "≊"
latex_symbols["\\backsim"] = "∽"
latex_symbols["\\vDash"] = "⊨"
latex_symbols["\\Vdash"] = "⊩"
latex_symbols["\\Vvdash"] = "⊪"
latex_symbols["\\backepsilon"] = "∍"
latex_symbols["\\varpropto"] = "∝"
latex_symbols["\\between"] = "≬"
latex_symbols["\\pitchfork"] = "⋔"
latex_symbols["\\blacktriangleleft"] = "◀"
latex_symbols["\\blacktriangleright"] = "▷"
latex_symbols["\\dashleftarrow"] = "⇠"
latex_symbols["\\leftleftarrows"] = "⇇"
latex_symbols["\\leftrightarrows"] = "⇆"
latex_symbols["\\Lleftarrow"] = "⇚"
latex_symbols["\\twoheadleftarrow"] = "↞"
latex_symbols["\\leftarrowtail"] = "↢"
latex_symbols["\\leftrightharpoons"] = "⇋"
latex_symbols["\\Lsh"] = "↰"
latex_symbols["\\looparrowleft"] = "↫"
latex_symbols["\\curvearrowleft"] = "↶"
latex_symbols["\\circlearrowleft"] = "↺"
latex_symbols["\\dashrightarrow"] = "⇢"
latex_symbols["\\rightrightarrows"] = "⇉"
latex_symbols["\\rightleftarrows"] = "⇄"
latex_symbols["\\Rrightarrow"] = "⇛"
latex_symbols["\\twoheadrightarrow"] = "↠"
latex_symbols["\\rightarrowtail"] = "↣"
latex_symbols["\\rightleftharpoons"] = "⇌"
latex_symbols["\\Rsh"] = "↱"
latex_symbols["\\looparrowright"] = "↬"
latex_symbols["\\curvearrowright"] = "↷"
latex_symbols["\\circlearrowright"] = "↻"
latex_symbols["\\multimap"] = "⊸"
latex_symbols["\\upuparrows"] = "⇈"
latex_symbols["\\downdownarrows"] = "⇊"
latex_symbols["\\upharpoonleft"] = "↿"
latex_symbols["\\upharpoonright"] = "↾"
latex_symbols["\\downharpoonleft"] = "⇃"
latex_symbols["\\downharpoonright"] = "⇂"
latex_symbols["\\rightsquigarrow"] = "⇝"
latex_symbols["\\leftrightsquigarrow"] = "↭"
latex_symbols["\\dotplus"] = "∔"
latex_symbols["\\ltimes"] = "⋉"
latex_symbols["\\Cup"] = "⋓"
latex_symbols["\\veebar"] = "⊻"
latex_symbols["\\boxplus"] = "⊞"
latex_symbols["\\boxtimes"] = "⊠"
latex_symbols["\\leftthreetimes"] = "⋋"
latex_symbols["\\curlyvee"] = "⋎"
latex_symbols["\\centerdot"] = "⋅"
latex_symbols["\\rtimes"] = "⋈"
latex_symbols["\\Cap"] = "⋒"
latex_symbols["\\barwedge"] = "⊼"
latex_symbols["\\boxminus"] = "⊟"
latex_symbols["\\boxdot"] = "⊡"
latex_symbols["\\rightthreetimes"] = "⋌"
latex_symbols["\\curlywedge"] = "⋏"
latex_symbols["\\intercal"] = "⊺"
latex_symbols["\\divideontimes"] = "⋇"
latex_symbols["\\smallsetminus"] = "∖"
latex_symbols["\\circleddash"] = "⊝"
latex_symbols["\\circledcirc"] = "⊚"
latex_symbols["\\circledast"] = "⊛"
latex_symbols["\\hbar"] = "ℏ"
latex_symbols["\\hslash"] = "ℏ"
latex_symbols["\\square"] = "□"
latex_symbols["\\blacksquare"] = "■"
latex_symbols["\\circledS"] = "Ⓢ"
latex_symbols["\\vartriangle"] = "△"
latex_symbols["\\blacktriangle"] = "▲"
latex_symbols["\\complement"] = "∁"
latex_symbols["\\triangledown"] = "▽"
latex_symbols["\\blacktriangledown"] = "▼"
latex_symbols["\\lozenge"] = "◊"
latex_symbols["\\blacklozenge"] = "◆"
latex_symbols["\\bigstar"] = "★"
latex_symbols["\\angle"] = "∠"
latex_symbols["\\measuredangle"] = "∡"
latex_symbols["\\sphericalangle"] = "∢"
latex_symbols["\\backprime"] = "‵"
latex_symbols["\\nexists"] = "∄"
latex_symbols["\\Finv"] = "Ⅎ"
latex_symbols["\\varnothing"] = "∅"
latex_symbols["\\eth"] = "ð"
latex_symbols["\\mho"] = "℧"
