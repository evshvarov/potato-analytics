/// 
Class esh.csvpkey.PotatoCube Extends %DeepSee.CubeDefinition [ DependsOn = esh.csvpkey.Potatos, ProcedureBlock ]
{

/// Cube definition from Architect.
XData Cube [ XMLNamespace = "http://www.intersystems.com/deepsee" ]
{
<cube xmlns="http://www.intersystems.com/deepsee" name="PotatoCube" displayName="Potatos Cube" disabled="false" abstract="false" sourceClass="esh.csvpkey.Potatos" namedFactNums="true" countMeasureName="%COUNT" bucketSize="8" bitmapChunkInMemory="false" precompute="0" disableListingGroups="false" enableSqlRestrict="false">
  <dimension name="Year" disabled="false" hasAll="false" allCaption="All Year" allDisplayName="Year" type="data" hidden="false" showHierarchies="default">
    <hierarchy name="H1" disabled="false" hidden="false">
      <level name="Year" disabled="false" sourceProperty="Year" list="false" useDisplayValue="true" useAsFilter="true" hidden="false" factNumber="2">
      </level>
    </hierarchy>
  </dimension>
  <dimension name="Country" disabled="false" hasAll="false" allCaption="All Country" allDisplayName="Country" type="data" hidden="false" showHierarchies="default">
    <hierarchy name="H1" disabled="false" hidden="false">
      <level name="Country" disabled="false" sourceProperty="Country" list="false" nullReplacement="Uknown Country" useDisplayValue="true" useAsFilter="true" hidden="false" factNumber="3">
        <property name="Name" disabled="false" sourceProperty="Country.Name" hidden="false" isName="true" isDescription="false" isReference="false" useDisplayValue="false">
        </property>
        <property name="Capital" disabled="false" sourceProperty="Country.Capital" hidden="false" isName="false" isDescription="false" isReference="false" useDisplayValue="false">
        </property>
        <property name="Latitude" disabled="false" sourceProperty="Country.Latitude" hidden="false" isName="false" isDescription="false" isReference="false" useDisplayValue="false">
        </property>
        <property name="Longitude" disabled="false" sourceProperty="Country.Longitude" hidden="false" isName="false" isDescription="false" isReference="false" useDisplayValue="false">
        </property>
      </level>
    </hierarchy>
  </dimension>
  <measure name="Potatoconsumptiontonnes" displayName="Potatos Consumption" disabled="false" sourceProperty="Potatoconsumptiontonnes" aggregate="SUM" type="integer" hidden="false" searchable="false" factNumber="1">
  </measure>
  <measure name="Potatoimporttonnes" displayName="Potatos Import" disabled="false" sourceProperty="Potatoimporttonnes" aggregate="SUM" type="integer" hidden="false" searchable="false" factNumber="2">
  </measure>
</cube>
}

Parameter DOMAIN;

ClassMethod EnableIRISBI(ns As %String) As %Status
{
  Set sc = $$$OK
  set ns=$g(ns) 
  if ns="" set ns=$ZNSPACE
  set ns=$$$LOWER(ns)
  do EnableDeepSee^%SYS.cspServer("/csp/"_ns_"/")
  Return sc
}

}
