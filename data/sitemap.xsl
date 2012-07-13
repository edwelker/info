<?xml version="1.0"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
<xsl:output method="xml" indent="yes"/>

    <xsl:variable name="lcletters">abcdefghijklmnopqrstuvwxyz</xsl:variable>
    <xsl:variable name="ucletters">ABCDEFGHIJKLMNOPQRSTUVWXYZ</xsl:variable>
    
    <xsl:variable name="aux" select="'pretty_sitemap.xml'"/>
    
    <xsl:template match="/">
        <resources>
            <xsl:apply-templates select="//Resource"/>
        </resources>
    </xsl:template>
    
    <xsl:template match="Resource">
        
            <!-- gets all of the resources -->
            <xsl:for-each select="Link">
                <xsl:variable name="t" select="."/>
                
                <xsl:choose>
                    <xsl:when test="document($aux)//url[. = $t]">
                        <resource>
                            <xsl:apply-templates select="../@*|../node()"/>
                            
                            <xsl:copy-of select="document($aux)//url[.=$t]/../categories"/>
                            <xsl:apply-templates select="document($aux)//url[.=$t]/../shortDesc"/>
                            <xsl:apply-templates select="document($aux)//url[.=$t]/../longDesc"/>
                        </resource>
                    </xsl:when>
                    
                    <xsl:otherwise>
                        <!--<url><xsl:value-of select="$t"/></url>
                        <xsl:if test="document($aux)//url[starts-with(., $t)]">
                            <from>
                                <xsl:value-of select="document($aux)//url[starts-with(., $t)]"/>
                            </from>
                            </xsl:if>-->
                        <resource>
                            <xsl:apply-templates select="../@*|../node()"/>
                        </resource>                      
                    </xsl:otherwise>
                </xsl:choose>
            </xsl:for-each>
        
            <!-- gotta deal with non-resources too, if there are any -->
        
<!--            <xsl:for-each select="document($aux)//resource/url">
                <xsl:variable name="t" select="."/>
                
                <xsl:choose>
                    <xsl:when test="//Resource/Link[. != $t]">
                        <xsl:value-of select="."/>
                    </xsl:when>
                    <xsl:otherwise>
                        <f/>
                    </xsl:otherwise>
                </xsl:choose>
            </xsl:for-each>-->
    </xsl:template>
    
    <xsl:template match="@*|node()">
        <xsl:copy>
            <xsl:apply-templates select="@*|node()"/>
        </xsl:copy>
    </xsl:template>

    <xsl:template match="shortDesc">
        <shortdesc>
            <xsl:value-of select="p"/>
        </shortdesc>
    </xsl:template>
    
    <xsl:template match="longDesc">
        <longdesc>
            <xsl:value-of select="p"/>
        </longdesc>
    </xsl:template>

</xsl:stylesheet>
