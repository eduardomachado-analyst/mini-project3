<div id="readme" class="Box-body readme blob js-code-block-container p-5 p-xl-6 gist-border-0">
    <article class="markdown-body entry-content container-lg" itemprop="text"><p><a target="_blank" rel="noopener noreferrer" href="https://camo.githubusercontent.com/7b53865828a6796cb5f25926548e18dbf5e14de2/68747470733a2f2f6269742e6c792f32566e58577232"><img src="https://camo.githubusercontent.com/7b53865828a6796cb5f25926548e18dbf5e14de2/68747470733a2f2f6269742e6c792f32566e58577232" width="100" data-canonical-src="https://bit.ly/2VnXWr2" style="max-width:100%;"></a></p>
<h1><a id="user-content-project-3--ethnic-analysis-of-brazilian-soap-operas" class="anchor" aria-hidden="true" href="#project-3--ethnic-analysis-of-brazilian-soap-operas"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7.775 3.275a.75.75 0 001.06 1.06l1.25-1.25a2 2 0 112.83 2.83l-2.5 2.5a2 2 0 01-2.83 0 .75.75 0 00-1.06 1.06 3.5 3.5 0 004.95 0l2.5-2.5a3.5 3.5 0 00-4.95-4.95l-1.25 1.25zm-4.69 9.64a2 2 0 010-2.83l2.5-2.5a2 2 0 012.83 0 .75.75 0 001.06-1.06 3.5 3.5 0 00-4.95 0l-2.5 2.5a3.5 3.5 0 004.95 4.95l1.25-1.25a.75.75 0 00-1.06-1.06l-1.25 1.25a2 2 0 01-2.83 0z"></path></svg></a>Project 3 | Ethnic Analysis of Brazilian Soap Operas</h1>
<p>Search for the names of all Rede Globo's soap operas, return the name of the cast and analyze the gender and ethnicity of the actors and actresses images.</p>
<h2><a id="user-content-soap-operas-names" class="anchor" aria-hidden="true" href="#soap-operas-names"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7.775 3.275a.75.75 0 001.06 1.06l1.25-1.25a2 2 0 112.83 2.83l-2.5 2.5a2 2 0 01-2.83 0 .75.75 0 00-1.06 1.06 3.5 3.5 0 004.95 0l2.5-2.5a3.5 3.5 0 00-4.95-4.95l-1.25 1.25zm-4.69 9.64a2 2 0 010-2.83l2.5-2.5a2 2 0 012.83 0 .75.75 0 001.06-1.06 3.5 3.5 0 00-4.95 0l-2.5 2.5a3.5 3.5 0 004.95 4.95l1.25-1.25a.75.75 0 00-1.06-1.06l-1.25 1.25a2 2 0 01-2.83 0z"></path></svg></a>Soap Operas Names</h2>
<p><a href="https://pypi.org/project/requests/" rel="nofollow">requests</a> allows you to send HTTP requests.<br>
<a href="https://pypi.org/project/beautifulsoup4/" rel="nofollow">beautifulsoup</a> to scrape information from web pages.</p>
<div class="highlight highlight-source-shell"><pre>pip install requests
pip install beautifulsoup4</pre></div>
<h2><a id="user-content-usage" class="anchor" aria-hidden="true" href="#usage"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7.775 3.275a.75.75 0 001.06 1.06l1.25-1.25a2 2 0 112.83 2.83l-2.5 2.5a2 2 0 01-2.83 0 .75.75 0 00-1.06 1.06 3.5 3.5 0 004.95 0l2.5-2.5a3.5 3.5 0 00-4.95-4.95l-1.25 1.25zm-4.69 9.64a2 2 0 010-2.83l2.5-2.5a2 2 0 012.83 0 .75.75 0 001.06-1.06 3.5 3.5 0 00-4.95 0l-2.5 2.5a3.5 3.5 0 004.95 4.95l1.25-1.25a.75.75 0 00-1.06-1.06l-1.25 1.25a2 2 0 01-2.83 0z"></path></svg></a>Usage</h2>
<div class="highlight highlight-source-python"><pre><span class="pl-k">import</span> <span class="pl-s1">pandas</span> <span class="pl-k">as</span> <span class="pl-s1">pd</span>
<span class="pl-k">import</span> <span class="pl-s1">requests</span>
<span class="pl-k">import</span> <span class="pl-s1">re</span>
<span class="pl-k">from</span> <span class="pl-s1">bs4</span> <span class="pl-k">import</span> <span class="pl-v">BeautifulSoup</span>

<span class="pl-s1">response</span> <span class="pl-c1">=</span> <span class="pl-s1">requests</span>.<span class="pl-en">get</span>(<span class="pl-s1">params</span>.<span class="pl-s1">novelas_url</span>)
<span class="pl-s1">html</span> <span class="pl-c1">=</span> <span class="pl-s1">response</span>.<span class="pl-s1">content</span>
<span class="pl-s1">soup</span> <span class="pl-c1">=</span> <span class="pl-v">BeautifulSoup</span>(<span class="pl-s1">html</span>)

<span class="pl-c"># Search for tables on the page</span>
<span class="pl-s1">tables</span> <span class="pl-c1">=</span> <span class="pl-s1">soup</span>.<span class="pl-en">find_all</span>(<span class="pl-s">'table'</span>, {<span class="pl-s">'class'</span>: <span class="pl-s">'wikitable'</span>})[<span class="pl-c1">35</span>:<span class="pl-c1">-</span><span class="pl-c1">1</span>]

<span class="pl-c"># Get the table with the name of soap operas and the aired year</span>
<span class="pl-s1">novelas_name</span> <span class="pl-c1">=</span> [<span class="pl-s1">tr</span>.<span class="pl-en">find</span>(<span class="pl-s">'i'</span>).<span class="pl-s1">text</span> <span class="pl-k">for</span> <span class="pl-s1">table</span> <span class="pl-c1">in</span> <span class="pl-s1">tables</span> <span class="pl-k">for</span> <span class="pl-s1">tr</span> <span class="pl-c1">in</span> <span class="pl-s1">table</span>.<span class="pl-en">find_all</span>(<span class="pl-s">'tr'</span>) <span class="pl-k">if</span> <span class="pl-s1">tr</span>.<span class="pl-en">find</span>(<span class="pl-s">'i'</span>)]
<span class="pl-s1">aired</span> <span class="pl-c1">=</span> [<span class="pl-s1">re</span>.<span class="pl-en">findall</span>(<span class="pl-s">'\d* \w+ \d\d*'</span>, <span class="pl-en">str</span>(<span class="pl-s1">tr</span>.<span class="pl-en">find_all</span>(<span class="pl-s">'td'</span>)))[<span class="pl-c1">0</span>] <span class="pl-k">for</span> <span class="pl-s1">table</span> <span class="pl-c1">in</span> <span class="pl-s1">tables</span> <span class="pl-k">for</span> <span class="pl-s1">tr</span> <span class="pl-c1">in</span> <span class="pl-s1">table</span>.<span class="pl-en">find_all</span>(<span class="pl-s">'tr'</span>) <span class="pl-k">if</span> <span class="pl-s1">tr</span>.<span class="pl-en">find_all</span>(<span class="pl-s">'td'</span>)]
<span class="pl-s1">novelas_df</span> <span class="pl-c1">=</span> <span class="pl-s1">pd</span>.<span class="pl-v">DataFrame</span>({<span class="pl-s">'novela_name'</span>: <span class="pl-s1">novel</span> <span class="pl-s1">as_name</span>, <span class="pl-s">'aired'</span>: <span class="pl-s1">aired</span>})</pre></div>
<h2><a id="user-content-casting-names" class="anchor" aria-hidden="true" href="#casting-names"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7.775 3.275a.75.75 0 001.06 1.06l1.25-1.25a2 2 0 112.83 2.83l-2.5 2.5a2 2 0 01-2.83 0 .75.75 0 00-1.06 1.06 3.5 3.5 0 004.95 0l2.5-2.5a3.5 3.5 0 00-4.95-4.95l-1.25 1.25zm-4.69 9.64a2 2 0 010-2.83l2.5-2.5a2 2 0 012.83 0 .75.75 0 001.06-1.06 3.5 3.5 0 00-4.95 0l-2.5 2.5a3.5 3.5 0 004.95 4.95l1.25-1.25a.75.75 0 00-1.06-1.06l-1.25 1.25a2 2 0 01-2.83 0z"></path></svg></a>Casting Names</h2>
<p><a href="https://pypi.org/project/wikipedia/" rel="nofollow">wikipedia</a> gets article summaries, get data like links and images from a page, and more.<br>
<a href="https://pypi.org/project/Unidecode/" rel="nofollow">unidecode</a> takes Unicode data and tries to represent it in ASCII characters</p>
<div class="highlight highlight-source-shell"><pre>pip install wikipedia
pip install Unidecode</pre></div>
<h2><a id="user-content-usage-1" class="anchor" aria-hidden="true" href="#usage-1"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7.775 3.275a.75.75 0 001.06 1.06l1.25-1.25a2 2 0 112.83 2.83l-2.5 2.5a2 2 0 01-2.83 0 .75.75 0 00-1.06 1.06 3.5 3.5 0 004.95 0l2.5-2.5a3.5 3.5 0 00-4.95-4.95l-1.25 1.25zm-4.69 9.64a2 2 0 010-2.83l2.5-2.5a2 2 0 012.83 0 .75.75 0 001.06-1.06 3.5 3.5 0 00-4.95 0l-2.5 2.5a3.5 3.5 0 004.95 4.95l1.25-1.25a.75.75 0 00-1.06-1.06l-1.25 1.25a2 2 0 01-2.83 0z"></path></svg></a>Usage</h2>
<div class="highlight highlight-source-python"><pre><span class="pl-k">import</span> <span class="pl-s1">wikipedia</span>
<span class="pl-k">import</span> <span class="pl-s1">pandas</span> <span class="pl-k">as</span> <span class="pl-s1">pd</span>
<span class="pl-k">import</span> <span class="pl-s1">unidecode</span>
<span class="pl-k">from</span> <span class="pl-s1">bs4</span> <span class="pl-k">import</span> <span class="pl-v">BeautifulSoup</span>

<span class="pl-s1">wikipedia</span>.<span class="pl-en">set_lang</span>(<span class="pl-s">"pt"</span>)

<span class="pl-s1">cast_df</span> <span class="pl-c1">=</span> <span class="pl-s1">pd</span>.<span class="pl-v">DataFrame</span>()

<span class="pl-c"># Search for the soap opera name and get the casting list</span>
<span class="pl-k">for</span> <span class="pl-s1">i</span>, <span class="pl-s1">row</span> <span class="pl-c1">in</span> <span class="pl-s1">novelas_df</span>.<span class="pl-en">iterrows</span>():
   <span class="pl-s1">soup</span> <span class="pl-c1">=</span> <span class="pl-c1">None</span>
      <span class="pl-k">try</span>:
         <span class="pl-s1">query</span> <span class="pl-c1">=</span> <span class="pl-s1">row</span>[<span class="pl-s">'novela_name'</span>] <span class="pl-c1">+</span> <span class="pl-s">' novela '</span> <span class="pl-c1">+</span> <span class="pl-s1">row</span>[<span class="pl-s">'aired'</span>][<span class="pl-c1">-</span><span class="pl-c1">4</span>:]
         <span class="pl-s1">soup</span> <span class="pl-c1">=</span> <span class="pl-v">BeautifulSoup</span>(<span class="pl-s1">wikipedia</span>.<span class="pl-en">page</span>(<span class="pl-s1">query</span>).<span class="pl-en">html</span>(), <span class="pl-s">'lxml'</span>)
      <span class="pl-k">except</span>:
         <span class="pl-k">try</span>:
            <span class="pl-s1">query</span> <span class="pl-c1">=</span> <span class="pl-s1">row</span>[<span class="pl-s">'novela_name'</span>] <span class="pl-c1">+</span> <span class="pl-s">' (telenovela) '</span> <span class="pl-c1">+</span> <span class="pl-s1">row</span>[<span class="pl-s">'aired'</span>][<span class="pl-c1">-</span><span class="pl-c1">4</span>:]
            <span class="pl-s1">soup</span> <span class="pl-c1">=</span> <span class="pl-v">BeautifulSoup</span>(<span class="pl-s1">wikipedia</span>.<span class="pl-en">page</span>(<span class="pl-s1">query</span>).<span class="pl-en">html</span>(), <span class="pl-s">'lxml'</span>)
         <span class="pl-k">except</span>:
             <span class="pl-en">print</span>(<span class="pl-s1">row</span>[<span class="pl-s">'novela_name'</span>])
      <span class="pl-k">if</span> <span class="pl-s1">soup</span>:
         <span class="pl-s1">foundid</span> <span class="pl-c1">=</span> <span class="pl-s1">soup</span>.<span class="pl-en">find</span>(<span class="pl-s">'span'</span>, {<span class="pl-s">'id'</span>: <span class="pl-s">'Elenco'</span>})
         <span class="pl-s1">table</span> <span class="pl-c1">=</span> <span class="pl-s1">foundid</span>.<span class="pl-en">findNext</span>(<span class="pl-s">'table'</span>)
         <span class="pl-s1">cast</span> <span class="pl-c1">=</span> [<span class="pl-s1">tr</span>.<span class="pl-en">find</span>(<span class="pl-s">'td'</span>).<span class="pl-s1">text</span>.<span class="pl-en">strip</span>().<span class="pl-en">replace</span>(<span class="pl-s">'<span class="pl-cce">\n</span>'</span>, <span class="pl-s">''</span>) <span class="pl-k">for</span> <span class="pl-s1">tr</span> <span class="pl-c1">in</span> <span class="pl-s1">table</span>.<span class="pl-en">find_all</span>(<span class="pl-s">'tr'</span>) <span class="pl-k">if</span> <span class="pl-s1">tr</span>.<span class="pl-en">find</span>(<span class="pl-s">'td'</span>)]
         <span class="pl-s1">cast_df</span> <span class="pl-c1">=</span> <span class="pl-s1">cast_df</span>.<span class="pl-en">join</span>(<span class="pl-s1">pd</span>.<span class="pl-v">DataFrame</span>({<span class="pl-s1">row</span>[<span class="pl-s">'novela_name'</span>]: <span class="pl-s1">cast</span>}), <span class="pl-s1">how</span><span class="pl-c1">=</span><span class="pl-s">'outer'</span>)

<span class="pl-c"># Remove the accentuation in names</span>
<span class="pl-k">for</span> <span class="pl-s1">i</span> <span class="pl-c1">in</span> <span class="pl-s1">cast_df</span>:
   <span class="pl-s1">cast_df</span>[<span class="pl-s1">i</span>] <span class="pl-c1">=</span> [<span class="pl-s1">unidecode</span>.<span class="pl-en">unidecode</span>(<span class="pl-en">str</span>(<span class="pl-s1">x</span>).<span class="pl-en">split</span>(<span class="pl-s">' ('</span>)[<span class="pl-c1">0</span>].<span class="pl-en">split</span>(<span class="pl-s">'['</span>)[<span class="pl-c1">0</span>].<span class="pl-en">strip</span>()) <span class="pl-k">for</span> <span class="pl-s1">x</span> <span class="pl-c1">in</span> <span class="pl-s1">cast_df</span>[<span class="pl-s1">i</span>]]

<span class="pl-c"># Replace nan string to type NaN</span>
<span class="pl-s1">cast_df</span> <span class="pl-c1">=</span> <span class="pl-s1">cast_df</span>[<span class="pl-s1">cast_df</span> <span class="pl-c1">!=</span> <span class="pl-s">'nan'</span>]

<span class="pl-s1">mask</span> <span class="pl-c1">=</span> <span class="pl-s1">cast_df</span>.<span class="pl-en">count</span>().<span class="pl-en">sort_values</span>() <span class="pl-c1">&lt;</span> <span class="pl-c1">30</span>
<span class="pl-s1">drop_cols</span> <span class="pl-c1">=</span> <span class="pl-s1">mask</span>[<span class="pl-s1">mask</span>].<span class="pl-s1">index</span>
<span class="pl-s1">cast_df</span> <span class="pl-c1">=</span> <span class="pl-s1">cast_df</span>.<span class="pl-en">drop</span>(<span class="pl-s1">drop_cols</span>, <span class="pl-s1">axis</span><span class="pl-c1">=</span><span class="pl-c1">1</span>)</pre></div>
<h2><a id="user-content-casting-images" class="anchor" aria-hidden="true" href="#casting-images"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7.775 3.275a.75.75 0 001.06 1.06l1.25-1.25a2 2 0 112.83 2.83l-2.5 2.5a2 2 0 01-2.83 0 .75.75 0 00-1.06 1.06 3.5 3.5 0 004.95 0l2.5-2.5a3.5 3.5 0 00-4.95-4.95l-1.25 1.25zm-4.69 9.64a2 2 0 010-2.83l2.5-2.5a2 2 0 012.83 0 .75.75 0 001.06-1.06 3.5 3.5 0 00-4.95 0l-2.5 2.5a3.5 3.5 0 004.95 4.95l1.25-1.25a.75.75 0 00-1.06-1.06l-1.25 1.25a2 2 0 01-2.83 0z"></path></svg></a>Casting Images</h2>
<p><a href="https://pypi.org/project/chromedriver_installer/" rel="nofollow">chromedriver</a> provides capabilities for navigating to web pages.</p>
<div class="highlight highlight-source-shell"><pre>pip install chromedriver_installer</pre></div>
<h2><a id="user-content-usage-2" class="anchor" aria-hidden="true" href="#usage-2"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7.775 3.275a.75.75 0 001.06 1.06l1.25-1.25a2 2 0 112.83 2.83l-2.5 2.5a2 2 0 01-2.83 0 .75.75 0 00-1.06 1.06 3.5 3.5 0 004.95 0l2.5-2.5a3.5 3.5 0 00-4.95-4.95l-1.25 1.25zm-4.69 9.64a2 2 0 010-2.83l2.5-2.5a2 2 0 012.83 0 .75.75 0 001.06-1.06 3.5 3.5 0 00-4.95 0l-2.5 2.5a3.5 3.5 0 004.95 4.95l1.25-1.25a.75.75 0 00-1.06-1.06l-1.25 1.25a2 2 0 01-2.83 0z"></path></svg></a>Usage</h2>
<div class="highlight highlight-source-python"><pre><span class="pl-k">import</span> <span class="pl-s1">os</span>
<span class="pl-k">import</span> <span class="pl-s1">requests</span>
<span class="pl-k">from</span> <span class="pl-s1">selenium</span> <span class="pl-k">import</span> <span class="pl-s1">webdriver</span>
<span class="pl-k">from</span> <span class="pl-s1">selenium</span>.<span class="pl-s1">webdriver</span>.<span class="pl-s1">support</span> <span class="pl-k">import</span> <span class="pl-s1">expected_conditions</span> <span class="pl-k">as</span> <span class="pl-v">EC</span>
<span class="pl-k">from</span> <span class="pl-s1">selenium</span>.<span class="pl-s1">webdriver</span>.<span class="pl-s1">support</span>.<span class="pl-s1">wait</span> <span class="pl-k">import</span> <span class="pl-v">WebDriverWait</span>

<span class="pl-s1">chrome_path</span> <span class="pl-c1">=</span> <span class="pl-s1">params</span>.<span class="pl-s1">chromedriver</span>

<span class="pl-c"># Open the chrome browser</span>
<span class="pl-s1">driver</span> <span class="pl-c1">=</span> <span class="pl-s1">webdriver</span>.<span class="pl-v">Chrome</span>(<span class="pl-s1">executable_path</span><span class="pl-c1">=</span><span class="pl-s1">chrome_path</span>)

<span class="pl-s1">file_path</span> <span class="pl-c1">=</span> <span class="pl-s1">os</span>.<span class="pl-s1">path</span>.<span class="pl-en">join</span>(<span class="pl-s1">params</span>.<span class="pl-s1">external_data</span>, <span class="pl-s">'/images/'</span>)

<span class="pl-c"># Get the casting names and search on Google images to get the first one</span>
<span class="pl-s1">cast_lst</span> <span class="pl-c1">=</span> <span class="pl-en">list</span>(<span class="pl-en">set</span>([<span class="pl-s1">x</span> <span class="pl-k">for</span> <span class="pl-s1">i</span> <span class="pl-c1">in</span> <span class="pl-s1">cast_df</span> <span class="pl-k">for</span> <span class="pl-s1">x</span> <span class="pl-c1">in</span> <span class="pl-s1">cast_df</span>[<span class="pl-s1">i</span>]]))

<span class="pl-k">for</span> <span class="pl-s1">i</span> <span class="pl-c1">in</span> <span class="pl-s1">cast_lst</span>:
   <span class="pl-c"># Search for names containing name and surename</span>
   <span class="pl-k">if</span> <span class="pl-en">len</span>(<span class="pl-s1">i</span>.<span class="pl-en">split</span>(<span class="pl-s">' '</span>)) <span class="pl-c1">&gt;</span> <span class="pl-c1">1</span>:
      <span class="pl-s1">url</span> <span class="pl-c1">=</span> (<span class="pl-s">f'https://www.google.com/search?as_st=y&amp;tbm=isch&amp;hl=pt-PT&amp;as_q="<span class="pl-s1"><span class="pl-kos">{</span><span class="pl-s1">i</span><span class="pl-kos">}</span></span>"+'</span>
                   
      <span class="pl-s">f'ator+atriz+"globo"+"novela"&amp;as_epq=&amp;as_oq=&amp;as_eq=&amp;cr=countryBR&amp;as_sitesearch='</span>
                   <span class="pl-s">f'&amp;safe=images&amp;tbs=ctr:countryBR,itp:face,ic:color '</span>)

      <span class="pl-c"># Navigate to webpage</span>
      <span class="pl-s1">driver</span>.<span class="pl-en">get</span>(<span class="pl-s1">url</span>)
      <span class="pl-s1">img</span> <span class="pl-c1">=</span> <span class="pl-v">WebDriverWait</span>(<span class="pl-s1">driver</span>, 
      <span class="pl-c1">3600</span>).<span class="pl-en">until</span>(<span class="pl-v">EC</span>.<span class="pl-en">presence_of_element_located</span>((<span class="pl-v">By</span>.<span class="pl-v">TAG_NAME</span>, <span class="pl-s">'img'</span>)))
      <span class="pl-s1">src</span> <span class="pl-c1">=</span> <span class="pl-s1">img</span>.<span class="pl-en">get_attribute</span>(<span class="pl-s">'src'</span>)

      <span class="pl-c"># Download the image</span>
      <span class="pl-s1">fullfilename</span> <span class="pl-c1">=</span> <span class="pl-s1">os</span>.<span class="pl-s1">path</span>.<span class="pl-en">join</span>(<span class="pl-s1">file_path</span>, <span class="pl-s">f'<span class="pl-s1"><span class="pl-kos">{</span><span class="pl-s1">i</span><span class="pl-kos">}</span></span>.jpg'</span>)
      <span class="pl-s1">urllib</span>.<span class="pl-s1">request</span>.<span class="pl-en">urlretrieve</span>(<span class="pl-s1">src</span>, <span class="pl-s1">fullfilename</span>)

<span class="pl-s1">driver</span>.<span class="pl-en">close</span>()</pre></div>
<h2><a id="user-content-haystack-api" class="anchor" aria-hidden="true" href="#haystack-api"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7.775 3.275a.75.75 0 001.06 1.06l1.25-1.25a2 2 0 112.83 2.83l-2.5 2.5a2 2 0 01-2.83 0 .75.75 0 00-1.06 1.06 3.5 3.5 0 004.95 0l2.5-2.5a3.5 3.5 0 00-4.95-4.95l-1.25 1.25zm-4.69 9.64a2 2 0 010-2.83l2.5-2.5a2 2 0 012.83 0 .75.75 0 001.06-1.06 3.5 3.5 0 00-4.95 0l-2.5 2.5a3.5 3.5 0 004.95 4.95l1.25-1.25a.75.75 0 00-1.06-1.06l-1.25 1.25a2 2 0 01-2.83 0z"></path></svg></a>Haystack API</h2>
<p><a href="https://www.haystack.ai/docs#api-reference" rel="nofollow">Haystack</a>. Ethnicity or race is detected and extracted based on large dataset.</p>
<div class="highlight highlight-source-shell"><pre>https://api.haystack.ai/api/image/analyze<span class="pl-k">?</span>output=json<span class="pl-k">&amp;</span>apikey=YOUR_KEY_HERE</pre></div>
<h2><a id="user-content-usage-3" class="anchor" aria-hidden="true" href="#usage-3"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7.775 3.275a.75.75 0 001.06 1.06l1.25-1.25a2 2 0 112.83 2.83l-2.5 2.5a2 2 0 01-2.83 0 .75.75 0 00-1.06 1.06 3.5 3.5 0 004.95 0l2.5-2.5a3.5 3.5 0 00-4.95-4.95l-1.25 1.25zm-4.69 9.64a2 2 0 010-2.83l2.5-2.5a2 2 0 012.83 0 .75.75 0 001.06-1.06 3.5 3.5 0 00-4.95 0l-2.5 2.5a3.5 3.5 0 004.95 4.95l1.25-1.25a.75.75 0 00-1.06-1.06l-1.25 1.25a2 2 0 01-2.83 0z"></path></svg></a>Usage</h2>
<div class="highlight highlight-source-python"><pre><span class="pl-k">import</span> <span class="pl-s1">os</span>
<span class="pl-k">import</span> <span class="pl-s1">requests</span>
<span class="pl-k">import</span> <span class="pl-s1">pandas</span> <span class="pl-k">as</span> <span class="pl-s1">pd</span>

<span class="pl-c"># List the filenames of the images</span>
<span class="pl-s1">files</span> <span class="pl-c1">=</span> <span class="pl-s1">os</span>.<span class="pl-en">listdir</span>(<span class="pl-s1">file_path</span>)

<span class="pl-c"># Apply the haystack API to analyze the race and gender</span>
<span class="pl-s1">df_data_cast</span> <span class="pl-c1">=</span> <span class="pl-s1">pd</span>.<span class="pl-v">DataFrame</span>()
<span class="pl-s1">not_found</span> <span class="pl-c1">=</span> <span class="pl-c1">0</span>
<span class="pl-k">for</span> <span class="pl-s1">i</span> <span class="pl-c1">in</span> <span class="pl-s1">files</span>:
   <span class="pl-k">try</span>:
      <span class="pl-s1">r</span> <span class="pl-c1">=</span> <span class="pl-s1">requests</span>.<span class="pl-en">post</span>(<span class="pl-s1">params</span>.<span class="pl-s1">haystackapi</span>, <span class="pl-s1">data</span><span class="pl-c1">=</span><span class="pl-en">open</span>(<span class="pl-s">f"<span class="pl-s1"><span class="pl-kos">{</span><span class="pl-s1">file_path</span><span class="pl-kos">}</span></span><span class="pl-s1"><span class="pl-kos">{</span><span class="pl-s1">i</span><span class="pl-kos">}</span></span>"</span>, <span class="pl-s">'rb'</span>))
      <span class="pl-s1">gender</span> <span class="pl-c1">=</span> <span class="pl-s1">r</span>.<span class="pl-en">json</span>()[<span class="pl-s">'people'</span>][<span class="pl-c1">0</span>][<span class="pl-s">'gender'</span>][<span class="pl-s">'gender'</span>]
      <span class="pl-s1">race</span> <span class="pl-c1">=</span> <span class="pl-s1">r</span>.<span class="pl-en">json</span>()[<span class="pl-s">'people'</span>][<span class="pl-c1">0</span>][<span class="pl-s">'ethnicity'</span>][<span class="pl-s">'ethnicity'</span>]
      <span class="pl-s1">df_race</span> <span class="pl-c1">=</span> <span class="pl-s1">pd</span>.<span class="pl-v">DataFrame</span>({<span class="pl-s">'name'</span>: [<span class="pl-s1">unidecode</span>.<span class="pl-en">unidecode</span>(<span class="pl-s1">i</span>[:<span class="pl-c1">-</span><span class="pl-c1">4</span>])], <span class="pl-s">'race'</span>: [<span class="pl-s1">race</span>], <span class="pl-s">'gender'</span>: [<span class="pl-s1">gender</span>]})
      <span class="pl-s1">df_data_cast</span> <span class="pl-c1">=</span> <span class="pl-s1">pd</span>.<span class="pl-en">concat</span>([<span class="pl-s1">df_data_cast</span>, <span class="pl-s1">df_race</span>])
   <span class="pl-k">except</span>:
      <span class="pl-s1">not_found</span> <span class="pl-c1">+=</span> <span class="pl-c1">1</span>

<span class="pl-c"># Separate by Black, Latin and White</span>
<span class="pl-s1">df_data_cast</span>[<span class="pl-s">'color'</span>] <span class="pl-c1">=</span> <span class="pl-s1">df_data_cast</span>[<span class="pl-s">'race'</span>].<span class="pl-en">apply</span>(<span class="pl-k">lambda</span> <span class="pl-s1">x</span>: <span class="pl-s">'Black'</span> <span class="pl-k">if</span> <span class="pl-s">'Black'</span> <span class="pl-c1">in</span> <span class="pl-s1">x</span> <span class="pl-k">else</span> (<span class="pl-s">'Latin'</span> <span class="pl-k">if</span> <span class="pl-s">'Latin'</span> <span class="pl-c1">in</span> <span class="pl-s1">x</span> <span class="pl-k">else</span> <span class="pl-s">'White'</span>))</pre></div>
<h2><a id="user-content-results" class="anchor" aria-hidden="true" href="#results"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7.775 3.275a.75.75 0 001.06 1.06l1.25-1.25a2 2 0 112.83 2.83l-2.5 2.5a2 2 0 01-2.83 0 .75.75 0 00-1.06 1.06 3.5 3.5 0 004.95 0l2.5-2.5a3.5 3.5 0 00-4.95-4.95l-1.25 1.25zm-4.69 9.64a2 2 0 010-2.83l2.5-2.5a2 2 0 012.83 0 .75.75 0 001.06-1.06 3.5 3.5 0 00-4.95 0l-2.5 2.5a3.5 3.5 0 004.95 4.95l1.25-1.25a.75.75 0 00-1.06-1.06l-1.25 1.25a2 2 0 01-2.83 0z"></path></svg></a>Results</h2>
<p><a href="https://public.tableau.com/profile/eduardo1414#!/vizhome/EthnicAnalysis/Story1?publish=yes" rel="nofollow">Tableau apresentation</a></p>
<ul>
<li><strong>116</strong> novels released since 2000</li>
<li><strong>101</strong> novels were used</li>
<li><strong>2289</strong> captured images</li>
<li><strong>2210</strong> actors / actresses successfully analyzed</li>
</ul>
<p><a target="_blank" rel="noopener noreferrer" href="https://github.com/eduardomachado-analyst/mini-project3/blob/master/2020-09-21_14h17_19.png"><img src="https://github.com/eduardomachado-analyst/mini-project3/raw/master/2020-09-21_14h17_19.png" alt="img" style="max-width:100%;"></a>
<a target="_blank" rel="noopener noreferrer" href="https://github.com/eduardomachado-analyst/mini-project3/blob/master/2020-09-21_14h23_00.png"><img src="https://github.com/eduardomachado-analyst/mini-project3/raw/master/2020-09-21_14h23_00.png" alt="img" style="max-width:100%;"></a></p>
<h3><a id="user-content-issues" class="anchor" aria-hidden="true" href="#issues"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7.775 3.275a.75.75 0 001.06 1.06l1.25-1.25a2 2 0 112.83 2.83l-2.5 2.5a2 2 0 01-2.83 0 .75.75 0 00-1.06 1.06 3.5 3.5 0 004.95 0l2.5-2.5a3.5 3.5 0 00-4.95-4.95l-1.25 1.25zm-4.69 9.64a2 2 0 010-2.83l2.5-2.5a2 2 0 012.83 0 .75.75 0 001.06-1.06 3.5 3.5 0 00-4.95 0l-2.5 2.5a3.5 3.5 0 004.95 4.95l1.25-1.25a.75.75 0 00-1.06-1.06l-1.25 1.25a2 2 0 01-2.83 0z"></path></svg></a>Issues</h3>
<ul>
<li>Some images may not match the actor / actress.</li>
<li>There may be errors due to the accuracy of the Machine Learning model for detecting ethnicities.</li>
</ul>
<h2><a id="user-content-source" class="anchor" aria-hidden="true" href="#source"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7.775 3.275a.75.75 0 001.06 1.06l1.25-1.25a2 2 0 112.83 2.83l-2.5 2.5a2 2 0 01-2.83 0 .75.75 0 00-1.06 1.06 3.5 3.5 0 004.95 0l2.5-2.5a3.5 3.5 0 00-4.95-4.95l-1.25 1.25zm-4.69 9.64a2 2 0 010-2.83l2.5-2.5a2 2 0 012.83 0 .75.75 0 001.06-1.06 3.5 3.5 0 00-4.95 0l-2.5 2.5a3.5 3.5 0 004.95 4.95l1.25-1.25a.75.75 0 00-1.06-1.06l-1.25 1.25a2 2 0 01-2.83 0z"></path></svg></a>Source</h2>
<p><a href="https://www.wikipedia.org/" rel="nofollow">Wikipedia</a><br>
<a href="https://www.google.com/" rel="nofollow">Google</a></p>
</article>
  </div>

    </div>
