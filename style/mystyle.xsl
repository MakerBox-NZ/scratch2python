<?xml version='1.0'?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="1.0">
  <xsl:import href="/usr/share/xml/docbook/xsl-stylesheets-1.78.1/fo/docbook.xsl"/>

  <xsl:template match="title" mode="chapter.titlepage.recto.auto.mode">  
    <fo:block xmlns:fo="http://www.w3.org/1999/XSL/Format" 
	      xsl:use-attribute-sets="chapter.titlepage.recto.style" 
	      margin-left="{$title.margin.left}"
	      color="#4381b2"
	      font-size="21pt"
	      font-weight="bold"
	      font-family="{$title.font.family}">
      <xsl:call-template name="component.title">
	<xsl:with-param name="node" select="ancestor-or-self::chapter[1]"/>
      </xsl:call-template>
    </fo:block>
  </xsl:template>

<!-- bridgehead -->

<xsl:attribute-set name="section.title.properties">
  <!--xsl:attribute name="font-family">
    <xsl:value-of select="$title.font.family"/>
  </xsl:attribute-->
  <xsl:attribute name="font-weight">bold</xsl:attribute>
    <xsl:attribute name="color">#4381b2</xsl:attribute>
  <!-- font size is calculated dynamically by section.heading template -->
  <xsl:attribute name="keep-with-next.within-column">always</xsl:attribute>
  <xsl:attribute name="text-align">left</xsl:attribute>
  <xsl:attribute name="margin-top">3em</xsl:attribute>
  <xsl:attribute name="space-before.minimum">0.8em</xsl:attribute>
  <xsl:attribute name="space-before.optimum">1.0em</xsl:attribute>
  <xsl:attribute name="space-before.maximum">1.2em</xsl:attribute>
</xsl:attribute-set>

<xsl:attribute-set name="section.title.level3.properties">
  <xsl:attribute name="font-weight">normal</xsl:attribute>
  <xsl:attribute name="font-style">normal</xsl:attribute>
  <xsl:attribute name="color">#4381b2</xsl:attribute>
  <xsl:attribute name="font-family">Prociono</xsl:attribute>
</xsl:attribute-set>

<xsl:attribute-set name="section.title.level4.properties">
  <xsl:attribute name="font-weight">normal</xsl:attribute>
  <xsl:attribute name="font-style">normal</xsl:attribute>
  <xsl:attribute name="color">#4381b2</xsl:attribute>
  <xsl:attribute name="font-family">Prociono</xsl:attribute>
</xsl:attribute-set>

<xsl:template match="emphasis[@role='strong']">
    <fo:block xmlns:fo="http://www.w3.org/1999/XSL/Format" 
	      font-weight="bold">
    <xsl:apply-templates/>
  </fo:block>
</xsl:template>

<!-- title page logo -->

<xsl:attribute-set name="informalexample.properties">
  <xsl:attribute name="text-align">center</xsl:attribute>
</xsl:attribute-set>

<!-- screen, programlisting -->

<xsl:attribute-set name="monospace.verbatim.properties">
    <xsl:attribute name="wrap-option">wrap</xsl:attribute>
    <xsl:attribute name="hyphenation-character">\</xsl:attribute>
</xsl:attribute-set>

<xsl:attribute-set name="shade.verbatim.style">
  <xsl:attribute name="background-color">#E0E0E0</xsl:attribute>
</xsl:attribute-set>

<!-- admonitions, breakout boxes -->

<xsl:template match="note">
  <xsl:variable name="id">
    <xsl:call-template name="object.id"/>
  </xsl:variable>
  <fo:block xmlns:fo="http://www.w3.org/1999/XSL/Format"
	    space-before.minimum="0.8em"
            space-before.optimum="1em"
            space-before.maximum="1.2em"
            start-indent="0.25in"
            end-indent="0.25in"
	    padding-top="6pt"
	    padding-bottom="2pt"
	    padding-left="4pt"
	    padding-right="4pt"
	    background-color="#ffdf5a">
    <xsl:if test="$admon.textlabel != 0 or title">
      <fo:block xmlns:fo="http://www.w3.org/1999/XSL/Format"
		keep-with-next='always'
		xsl:use-attribute-sets="admonition.title.properties"
		font-family="Prociono"
		color="#4381b2"
		font-weight="bold">
         <xsl:apply-templates select="." mode="object.title.markup"/>
      </fo:block>
    </xsl:if>

    <fo:block xmlns:fo="http://www.w3.org/1999/XSL/Format"
	      xsl:use-attribute-sets="admonition.properties"
	      font-family="Prociono">
      <xsl:apply-templates/>
    </fo:block> 
  </fo:block>
</xsl:template>

<xsl:template match="warning">
  <xsl:variable name="id">
    <xsl:call-template name="object.id"/>
  </xsl:variable>
  <fo:block xmlns:fo="http://www.w3.org/1999/XSL/Format"
	    space-before.minimum="0.8em"
            space-before.optimum="1em"
            space-before.maximum="1.2em"
            start-indent="0.25in"
            end-indent="0.25in"
	    padding-top="6pt"
	    padding-bottom="2pt"
	    padding-left="4pt"
	    padding-right="4pt"
	    background-color="#FFDBE6">
    <xsl:if test="$admon.textlabel != 0 or title">
      <fo:block xmlns:fo="http://www.w3.org/1999/XSL/Format"
		keep-with-next='always'
		xsl:use-attribute-sets="admonition.title.properties"
		font-family="Prociono"
		color="#9A1A1C"
		font-weight="bold">
         <xsl:apply-templates select="." mode="object.title.markup"/>
      </fo:block>
    </xsl:if>

    <fo:block xmlns:fo="http://www.w3.org/1999/XSL/Format"
	      xsl:use-attribute-sets="admonition.properties"
	      font-family="Prociono">
      <xsl:apply-templates/>
    </fo:block> 
  </fo:block>
</xsl:template>

<!-- page break -->

<xsl:template match="processing-instruction('hard-pagebreak')">
  <fo:block xmlns:fo="http://www.w3.org/1999/XSL/Format"
	    break-after='page'/>  
</xsl:template>

<!-- image span 

<xsl:attribute-set name="pgwide.properties">
  <xsl:attribute name="span">all</xsl:attribute>
  <xsl:attribute name="padding-top">0pt</xsl:attribute>
  <xsl:attribute name="padding-bottom">0pt</xsl:attribute>
</xsl:attribute-set>

<xsl:attribute-set name="component.titlepage.properties">
  <xsl:attribute name="span">all</xsl:attribute>
</xsl:attribute-set -->

<!-- footer -->

<xsl:template name="redist.text">
    <xsl:choose>
      <xsl:when test="$redist.text = 'sa'">
	<xsl:text>Creative Commons BY-SA</xsl:text>  
      </xsl:when>

      <xsl:when test="$redist.text = 'nc'">
	<xsl:text>Creative Commons BY-NC</xsl:text>  
      </xsl:when>

      <xsl:when test="$redist.text = 'ncnd'">
	<xsl:text>Creative Commons BY-NC-ND</xsl:text>  
      </xsl:when>

      <xsl:when test="$redist.text = 'nd'">
	<xsl:text>Creative Commons BY-ND</xsl:text>  
      </xsl:when>
    </xsl:choose>
</xsl:template>

<xsl:attribute-set name="footer.table.properties">
  <xsl:attribute name="padding-left">5pt</xsl:attribute>
  <xsl:attribute name="font-family">Prociono</xsl:attribute>
  <xsl:attribute name="padding-right">5pt</xsl:attribute>
  <xsl:attribute name="font-size">8</xsl:attribute>
  <xsl:attribute name="font-weight">italics</xsl:attribute>
</xsl:attribute-set>


<xsl:template name="footer.content">  
  <xsl:param name="pageclass" select="''"/>
  <xsl:param name="sequence" select="''"/>
  <xsl:param name="position" select="''"/>
  <xsl:param name="gentext-key" select="''"/>

  <fo:block xmlns:fo="http://www.w3.org/1999/XSL/Format">  
    <!-- sequence can be odd, even, first, blank -->
    <!-- position can be left, center, right -->
    <xsl:choose>

      <xsl:when test="$sequence = 'odd' and $position = 'left'">  
        <xsl:call-template name="redist.text"/>  
      </xsl:when>

      <xsl:when test="$sequence = 'odd' and $position = 'center'">
      </xsl:when>

      <xsl:when test="$sequence = 'odd' and $position = 'right'">
        <fo:page-number/>  
      </xsl:when>

      <xsl:when test="$sequence = 'even' and $position = 'left'">  
        <fo:page-number/>
      </xsl:when>

      <xsl:when test="$sequence = 'even' and $position = 'center'">
      </xsl:when>

      <xsl:when test="$sequence = 'even' and $position = 'right'">
        <xsl:call-template name="redist.text"/>  
      </xsl:when>

      <xsl:when test="$sequence = 'first' and $position = 'left'"> 
        <xsl:call-template name="redist.text"/>  
      </xsl:when>

      <xsl:when test="$sequence = 'first' and $position = 'right'">  
        <fo:page-number/>
      </xsl:when>

      <xsl:when test="$sequence = 'first' and $position = 'center'"> 
      </xsl:when>

      <xsl:when test="$sequence = 'blank' and $position = 'left'">
        <fo:page-number/>
      </xsl:when>

      <xsl:when test="$sequence = 'blank' and $position = 'center'">
        <xsl:text>This page intentionally left blank</xsl:text>  
      </xsl:when>

      <xsl:when test="$sequence = 'blank' and $position = 'right'">
      </xsl:when>

    </xsl:choose>
  </fo:block>
</xsl:template>

</xsl:stylesheet>
