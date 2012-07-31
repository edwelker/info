<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    version="1.0">
    
    <xsl:template match="resource-index">
        <resources>
            <xsl:apply-templates select="//resource"/>
        </resources>
    </xsl:template>
    
    <xsl:template match="shortDesc/p|longDesc/p">
        <xsl:copy-of select="node()"/>
    </xsl:template>
    
    <xsl:template match="@*|node()">
        <xsl:copy>
            <xsl:apply-templates select="@*|node()"/>
        </xsl:copy>
    </xsl:template>
    
</xsl:stylesheet>