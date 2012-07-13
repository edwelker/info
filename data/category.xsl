<?xml version="1.0"?>
<xsl:stylesheet version="1.0"
xmlns:xsl="http://www.w3.org/1999/XSL/Transform">

    <xsl:template match="categories">
        <django-objects version="1.0">
            <xsl:apply-templates/>
        </django-objects>
    </xsl:template>

    <xsl:template match="category">
        <object pk="{url}" model="web_resources.category">
            <field type="CharField" name="display_name">
                <xsl:apply-templates select="title"/>
            </field>
        </object>
    </xsl:template>


</xsl:stylesheet>
