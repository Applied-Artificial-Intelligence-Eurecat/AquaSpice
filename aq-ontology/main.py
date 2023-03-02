from owlready2 import *

from datetime import datetime

def CS1_IparkDOW (wsisSchema):
    saref4water = get_namespace("https://saref.etsi.org/saref4watr/")
    saref = get_namespace("https://saref.etsi.org/core/")
    om = get_namespace("http://www.ontology-of-units-of-measure.org/resource/om-2/")

    mlperLitter = om.PrefixedGramPerLitre("milligramPerLitre")

    iparkdow = wsisSchema.Industry("iParkDOw")
    iparkdow.hasName.append("I-PARC DOW TERNEUZEN ")
    iparkdow.hasDescription.append("Dow's businesses include specialty chemicals, advanced materials and plastics. They offer technology-based products and services to clients in about 160 countries and in high growth sectors like food and specialty packaging, industrial and consumer packaging, health and hygiene, electronics, energy, architectural and industrial coatings, home care and personal care, as well as infrastructure.")
    iparkdow.hasOwner.append("DOW Chemicals")

    GranularActivatedCarbon = wsisSchema.Technology("GAP")
    GranularActivatedCarbon.hasName.append("Granular Activated Carbon")
    GranularActivatedCarbon.hasDescription.append("Granular activated carbon is made from raw organic materials (such as coconut shells or coal) that are high in carbon. Heat, in the absence of oxygen, is used to increase (activate) the surface area of the carbon; this is why these filters are sometimes referred to as “charcoal” filters.")
    iparkdow.usesTechnology.append(GranularActivatedCarbon)

    water_gap = saref4water.Water("WaterInputGAP")
    GranularActivatedCarbon.canProcess.append(water_gap)
    water_output_gap = saref4water.Water("WaterOutputGAP")
    GranularActivatedCarbon.generates.append(water_output_gap)

    UF = wsisSchema.Technology("Ultrafiltration")
    UF.hasName.append("Ultra-Fitration Technology")
    UF.hasDescription.append("Ultrafiltration (UF) is a pressure-driven purification process that separates particulate matter from soluble compounds using an ultrafine membrane media.")
    UF.canProcess.append(water_output_gap)
    water_output_uf = saref4water.Water("WaterOutputUF")
    UF.generates.append(water_output_uf)

    RO = wsisSchema.Technology("ReverseOsmosis")
    RO.hasName.append("Reverse Osmosis Technology")
    RO.hasDescription.append(
        "Reverse Osmosis is a technology that is used to remove a large majority of contaminants from water by pushing the water under pressure through a semi-permeable membrane.")
    RO.canProcess.append(water_output_uf)
    water_output_ro = saref4water.Water("WaterOutputRO")
    RO.generates.append(water_output_ro)

    FlowRateMeasurement = saref.Measurement("FlowRateMeasurement")
    cubicMetrePerHour = saref.UnitOfMeasure("cubicMetrePerHour")
    cubicMetrePerHour.hasName.append("m^3/h")
    FlowRateMeasurement.isMeasuredIn.append(cubicMetrePerHour)
    FlowRateMeasurement.relatesToProperty.append(saref4water.FlowRate)
    iparkdow.hasMeasurement.append(FlowRateMeasurement)

    TemperatureMeasurement = saref.Measurement("TemperatureMeasurement")
    TemperatureMeasurement.isMeasuredIn.append(om.centidegreeCelsius)
    TemperatureMeasurement.relatesToProperty.append(saref4water.FlowTemperature)
    iparkdow.hasMeasurement.append(TemperatureMeasurement)

    TOCMeasurement = saref.Measurement("TOCMeasurement")
    TOC = saref4water.AcceptabilityProperty("TotalOrganicCarbon")
    TOC.hasName.append("Total Organic Carbon")
    TOCMeasurement.isMeasuredIn.append(mlperLitter)
    TOCMeasurement.relatesToProperty.append(TOC)
    iparkdow.hasMeasurement.append(TOCMeasurement)

    ConductivityMeasurement = saref.Measurement("ConductivityMeasurement")
    microSiemmensPerCm = saref.UnitOfMeasure("microSiemmensPerCm")
    microSiemmensPerCm.hasName.append("\u03BCS/cm")
    ConductivityMeasurement.isMeasuredIn.append(microSiemmensPerCm)
    ConductivityMeasurement.relatesToProperty.append(saref4water.Conductivity)
    iparkdow.hasMeasurement.append(ConductivityMeasurement)

    TurbidityMeasurement = saref.Measurement("TurbidityMeasurement")
    FTU = saref.UnitOfMeasure("FTU")
    FTU.hasName.append("Formazine Turbidity Unit")
    FTU.hasDescription.append(
        "FTU became the defined unit of measurement after the acceptance of Formazine as the primary reference standard for turbidity. FTU, as well as any measurement unit derived from, or that references FTU does not specify how a device measures turbidity in a water sample")
    TurbidityMeasurement.isMeasuredIn.append(FTU)
    TurbidityMeasurement.relatesToProperty.append(saref4water.Turbidity)
    iparkdow.hasMeasurement.append(TurbidityMeasurement)

    PhosphateMeasurement = saref.Measurement("PhosphateMeasurement")
    Phosphate =saref4water.ChemicalProperty("Phosphate")
    Phosphate.hasName.append("Phosphate")
    Phosphate.hasDescription.append("A phosphate is an anion, salt, functional group or ester derived from a phosphoric acid.")
    PhosphateMeasurement.isMeasuredIn.append(mlperLitter)
    PhosphateMeasurement.relatesToProperty.append(Phosphate)
    iparkdow.hasMeasurement.append(PhosphateMeasurement)

    CalciumMeasurement = saref.Measurement("CalciumMeasurement")
    CalciumMeasurement.isMeasuredIn.append(mlperLitter)
    CalciumMeasurement.relatesToProperty.append(saref4water.Cadmium)
    iparkdow.hasMeasurement.append(CalciumMeasurement)

    MagnesiumMeasurement = saref.Measurement("MagnesiumMeasurement")
    Magnesium = saref4water.ChemicalProperty("Magnesium")
    Magnesium.hasName.append("Magnesium")
    Magnesium.hasDescription.append(
        "the chemical element of atomic number 12, a silver-white metal of the alkaline earth series. It is used to make strong lightweight alloys, and is also used in flash bulbs and pyrotechnics, as it burns with a brilliant white flame.")
    MagnesiumMeasurement.isMeasuredIn.append(mlperLitter)
    MagnesiumMeasurement.relatesToProperty.append(Magnesium)
    iparkdow.hasMeasurement.append(MagnesiumMeasurement)

    PotasiumMeasurement = saref.Measurement("PotasiumMeasurement")
    Potasium = saref4water.ChemicalProperty("Magnesium")
    Potasium.hasName.append("Magnesium")
    Potasium.hasDescription.append(
        "the chemical element of atomic number 19, a soft silvery-white reactive metal of the alkali metal group.")
    PotasiumMeasurement.isMeasuredIn.append(mlperLitter)
    PotasiumMeasurement.relatesToProperty.append(Potasium)
    iparkdow.hasMeasurement.append(PotasiumMeasurement)

    SodiumMeasurement = saref.Measurement("SodiumMeasurement")
    SodiumMeasurement.isMeasuredIn.append(mlperLitter)
    SodiumMeasurement.relatesToProperty.append(saref4water.Sodium)
    iparkdow.hasMeasurement.append(SodiumMeasurement)

    ZincMeasurement = saref.Measurement("ZincMeasurement")
    Zinc = saref4water.ChemicalProperty("Zinc")
    Zinc.hasName.append("Zinc")
    Zinc.hasDescription.append(
        "the chemical element of atomic number 30, a silvery-white metal that is a constituent of brass and is used for coating (galvanizing) iron and steel to protect against corrosion.")
    ZincMeasurement.isMeasuredIn.append(mlperLitter)
    ZincMeasurement.relatesToProperty.append(Zinc)
    iparkdow.hasMeasurement.append(ZincMeasurement)

    BariumMeasurement = saref.Measurement("BariumMeasurement")
    Barium = saref4water.ChemicalProperty("Barium")
    Barium.hasName.append("Barium")
    Barium.hasDescription.append(
        "the chemical element of atomic number 56, a soft white reactive metal of the alkaline earth group.")
    BariumMeasurement.isMeasuredIn.append(mlperLitter)
    BariumMeasurement.relatesToProperty.append(Zinc)
    iparkdow.hasMeasurement.append(BariumMeasurement)

    ManganeseMeasurement = saref.Measurement("ManganeseMeasurement")
    ManganeseMeasurement.isMeasuredIn.append(mlperLitter)
    ManganeseMeasurement.relatesToProperty.append(saref4water.Manganese)
    iparkdow.hasMeasurement.append(ManganeseMeasurement)

    AluminiumMeasurement = saref.Measurement("AluminiumMeasurement")
    AluminiumMeasurement.isMeasuredIn.append(mlperLitter)
    AluminiumMeasurement.relatesToProperty.append(saref4water.Aluminium)
    iparkdow.hasMeasurement.append(AluminiumMeasurement)

    IronMeasurement = saref.Measurement("IronMeasurement")
    IronMeasurement.isMeasuredIn.append(mlperLitter)
    IronMeasurement.relatesToProperty.append(saref4water.Aluminium)
    iparkdow.hasMeasurement.append(IronMeasurement)

    MethylBenzotriazoleMeasurement = saref.Measurement("MethylBenzotriazoleMeasurement")
    MethylBenzotriazole = saref4water.ChemicalProperty("MethylBenzotriazole")
    MethylBenzotriazole.hasName.append("MethylBenzotriazole")
    MethylBenzotriazole.hasDescription.append(
        "Benzotriazole (BTA) is a heterocyclic compound with the chemical formula C6H5N3. Its five-membered ring contains three consecutive nitrogen atoms.")
    microgrampPerLiter = saref.UnitOfMeasure("microgrampPerLiter")
    microgrampPerLiter.hasName.append("\u03BCg/L")
    MethylBenzotriazoleMeasurement.isMeasuredIn.append(microgrampPerLiter)
    MethylBenzotriazoleMeasurement.relatesToProperty.append(MethylBenzotriazole)
    iparkdow.hasMeasurement.append(MethylBenzotriazoleMeasurement)

    BenzotriazoleMeasurement = saref.Measurement("MethylBenzotriazoleMeasurement")
    BenzotriazoleMeasurement.isMeasuredIn.append(microgrampPerLiter)
    BenzotriazoleMeasurement.relatesToProperty.append(MethylBenzotriazole)
    iparkdow.hasMeasurement.append(BenzotriazoleMeasurement)

    AOXMeasurement = saref.Measurement("AOXMeasurement")
    AOX = saref4water.AcceptabilityProperty("AOX")
    AOX.hasName.append("Adsorbable Organically bound halogens")
    AOX.hasDescription.append("Adsorbable Organic Halides (AOX) is a measure of the organic halogen load at a sampling site such as soil from a land fill, water, or sewage waste.")
    AOXMeasurement.isMeasuredIn.append(mlperLitter)
    AOXMeasurement.relatesToProperty.append(AOX)
    iparkdow.hasMeasurement.append(BenzotriazoleMeasurement)

    ChlorideMeasurement = saref.Measurement("ChlorideMeasurement")
    ChlorideMeasurement.isMeasuredIn.append(mlperLitter)
    ChlorideMeasurement.relatesToProperty.append(saref4water.Chloride)
    iparkdow.hasMeasurement.append(ChlorideMeasurement)

    IronMeasurement = saref.Measurement("IronMeasurement")
    IronMeasurement.isMeasuredIn.append(mlperLitter)
    IronMeasurement.relatesToProperty.append(saref4water.Iron)
    iparkdow.hasMeasurement.append(IronMeasurement)

    NH3Measurement = saref.Measurement("NH3Measurement")
    Ammonia = saref4water.ChemicalProperty("Ammonia")
    Ammonia.hasName.append("Ammonia")
    Ammonia.hasDescription.append("A gas with a strong, unpleasant smell used in making explosives, fertilizers")
    NH3Measurement.isMeasuredIn.append(mlperLitter)
    NH3Measurement.relatesToProperty.append(Ammonia)
    iparkdow.hasMeasurement.append(NH3Measurement)

    NitrateNitrogenMeasurement = saref.Measurement("NitrateNitrogenMeasurement")
    NitrateNitrogen = saref4water.ChemicalProperty("NitrateNitrogen")
    NitrateNitrogen.hasName.append("NitrateNitrogen")
    NitrateNitrogen.hasDescription.append("Nitrate is a chemical compound that includes nitrogen and oxygen.")
    NitrateNitrogenMeasurement.isMeasuredIn.append(mlperLitter)
    NitrateNitrogenMeasurement.relatesToProperty.append(NitrateNitrogen)
    iparkdow.hasMeasurement.append(NitrateNitrogenMeasurement)

    SulfateMeasurement = saref.Measurement("SulfateMeasurement")
    Sulfate = saref4water.ChemicalProperty("Sulfate")
    Sulfate.hasName.append("Sulfate")
    Sulfate.hasDescription.append("a chemical formed from sulphur, oxygen, and another element")
    SulfateMeasurement.isMeasuredIn.append(mlperLitter)
    SulfateMeasurement.relatesToProperty.append(Sulfate)
    iparkdow.hasMeasurement.append(SulfateMeasurement)

    LegionellaMeasurement = saref.Measurement("LegionellaMeasurement")
    Legionella = saref4water.BacterialProperty("Legionella")
    Legionella.hasName.append("Legionella")
    Legionella.hasDescription.append(
        "Legionella is a genus of pathogenic gram-negative bacteria that includes the species L. pneumophila, ")
    LegionellaMeasurement.isMeasuredIn.append(mlperLitter)
    LegionellaMeasurement.relatesToProperty.append(NitrateNitrogen)
    iparkdow.hasMeasurement.append(LegionellaMeasurement)

    return wsisSchema

def CS1_DOW_Bohlen(wsisSchema):
    saref4water = get_namespace("https://saref.etsi.org/saref4watr/")
    saref = get_namespace("https://saref.etsi.org/core/")
    om = get_namespace("http://www.ontology-of-units-of-measure.org/resource/om-2/")

    mlperLitter = om.PrefixedGramPerLitre("milligramPerLitre")

    dow = wsisSchema.Industry("DowBohlen")
    dow.hasName.append("DOW-BOHLEN")
    dow.hasDescription.append(
        "The location Böhlen strives to reduce its freshwater intake intensity by (a) enhancing the internal recycling of various process water streams – these comprise (but are not limited to) cooling tower blowdown and steam production blowdown streams, and (b) creating the next level of site water management by using smart monitoring, algorithms and control on raw water, discharge and recycle streams.")
    dow.hasOwner.append("DOW Chemicals")

    trialTestInfrastructure1 = wsisSchema.Technology("TestInfrastructure1")
    trialTestInfrastructure1.hasName.append("Test Infrastructure 1")
    trialTestInfrastructure1.hasDescription.append("Test Infrastructure 1: Current Infrastructure + UF + RO+ MB")

    currentInfrastructure = wsisSchema.Technology("CurrentInfrastructure")
    currentInfrastructure.hasName.append("Current Infrastructure")
    trialTestInfrastructure1.usesTechnology.append(currentInfrastructure)

    water_operation = saref4water.Water("WaterOperation")
    trialTestInfrastructure1.canProcess.append(water_operation)
    waterCurrentInfrastructure = saref4water.Water("WaterCurrentInfrastruture")
    trialTestInfrastructure1.generates.append(waterCurrentInfrastructure)

    UF = wsisSchema.Technology("Ultrafiltration")
    UF.hasName.append("Ultra-Fitration Technology")
    UF.hasDescription.append(
        "Ultrafiltration (UF) is a pressure-driven purification process that separates particulate matter from soluble compounds using an ultrafine membrane media.")
    UF.canProcess.append(waterCurrentInfrastructure)
    water_output_uf = saref4water.Water("WaterOutputUF")
    UF.generates.append(water_output_uf)

    RO = wsisSchema.Technology("ReverseOsmosis")
    RO.hasName.append("Reverse Osmosis Technology")
    RO.hasDescription.append(
        "Reverse Osmosis is a technology that is used to remove a large majority of contaminants from water by pushing the water under pressure through a semi-permeable membrane.")
    RO.canProcess.append(water_output_uf)
    water_output_ro = saref4water.Water("WaterOutputRO")
    RO.generates.append(water_output_ro)

    MB = wsisSchema.Technology("MixedBed")
    MB.hasName.append("Mixed Bed")
    MB.hasDescription.append("Mixed Bed Units are an ion exchange method used where superior water quality is needed")
    MB.canProcess.append(water_output_ro)
    water_output_mb = saref4water.Water("WaterOutputMB")
    MB.generates.append(water_output_mb)

    EDR = wsisSchema.Technology("EDR")
    EDR.hasName.append("Electrodialysis Reversal")
    EDR.description.append("Electrodialysis reversal (EDR) is an electrodialysis reversal water desalination membrane process that has been commercially used since the early 1960s.")
    EDR.canProcess.append(water_output_uf)
    water_output_edr= saref4water.Water("waterOutputEDR")
    EDR.generates.append(water_output_edr)

    FlowRateMeasurement = saref.Measurement("FlowRateMeasurement")
    cubicMetrePerHour = saref.UnitOfMeasure("cubicMetrePerHour")
    cubicMetrePerHour.hasName.append("m^3/h")
    FlowRateMeasurement.isMeasuredIn.append(cubicMetrePerHour)
    FlowRateMeasurement.relatesToProperty.append(saref4water.FlowRate)
    trialTestInfrastructure1.hasMeasurement.append(FlowRateMeasurement)

    TemperatureMeasurement = saref.Measurement("TemperatureMeasurement")
    TemperatureMeasurement.isMeasuredIn.append(om.centidegreeCelsius)
    TemperatureMeasurement.relatesToProperty.append(saref4water.FlowTemperature)
    trialTestInfrastructure1.hasMeasurement.append(TemperatureMeasurement)

    TOCMeasurement = saref.Measurement("TOCMeasurement")
    TOC = saref4water.AcceptabilityProperty("TotalOrganicCarbon")
    TOC.hasName.append("Total Organic Carbon")
    TOCMeasurement.isMeasuredIn.append(mlperLitter)
    TOCMeasurement.relatesToProperty.append(TOC)
    trialTestInfrastructure1.hasMeasurement.append(TOCMeasurement)

    ConductivityMeasurement = saref.Measurement("ConductivityMeasurement")
    microSiemmensPerCm = saref.UnitOfMeasure("microSiemmensPerCm")
    microSiemmensPerCm.hasName.append("\u03BCS/cm")
    ConductivityMeasurement.isMeasuredIn.append(microSiemmensPerCm)
    ConductivityMeasurement.relatesToProperty.append(saref4water.Conductivity)
    trialTestInfrastructure1.hasMeasurement.append(ConductivityMeasurement)

    CODMeasurement = saref.Measurement("CODMeasurement")
    totalCOD = saref4water.AcceptabilityProperty("COD")
    totalCOD.hasName.append("Chemical Oxigen Demand")
    totalCOD.hasDescription.append(
        "The COD is the estimate of oxygen required for the portion of organic matter in wastewater that is subjected to oxidation and also the amount of oxygen consumed by organic matter from boiling acid potassium dichromate solution.")
    CODMeasurement.relatesToProperty.append(totalCOD)
    mlperLitter = om.PrefixedGramPerLitre("milligramPerLitre")
    CODMeasurement.isMeasuredIn.append(mlperLitter)

    TCMeasurement = saref.Measurement("TCMeasurement")
    TC = saref4water.AcceptabilityProperty("TC")
    TC.hasName.append("Total Chlorine")
    TC.hasDescription.append(
        "TC (Total Chlorine) water measurement is a method used to determine the amount of chlorine present in water. Chlorine is often added to water as a disinfectant to kill bacteria and other harmful microorganisms. The amount of chlorine present in the water is typically measured in parts per million (ppm) or milligrams per liter (mg/L). The measurement of TC is important in ensuring that the water is safe to drink and that the appropriate amount of chlorine is being used")
    TCMeasurement.isMeasuredIn.append(mlperLitter)
    TCMeasurement.relatesToProperty.append(TC)
    trialTestInfrastructure1.hasMeasurement.append(TCMeasurement)

    TICMeasurement = saref.Measurement("TICMeasurement")
    TIC = saref4water.AcceptabilityProperty("TIC")
    TIC.hasName.append("Total Inorganic Carbon")
    TIC.hasDescription.append(
        "TIC (Total Inorganic Carbon) water measurement is a method used to determine the total amount of inorganic dissolved carbon present in water. It is often used in water treatment plants, laboratories, and research studies to monitor the quality of drinking water, surface water, and groundwater. The TIC measurement is important in understanding the carbon chemistry of the water, including pH, alkalinity, and dissolved CO2. TIC is typically measured in milligrams per liter (mg/L) or parts per million (ppm). The measurement of TIC is also important in understanding the sources of carbon in the water and how it may be impacting aquatic life.")
    TICMeasurement.isMeasuredIn.append(mlperLitter)
    TICMeasurement.relatesToProperty.append(TIC)
    trialTestInfrastructure1.hasMeasurement.append(TICMeasurement)

    BODMeasurement = saref.Measurement("BODMeasurement")
    BOD = saref4water.AcceptabilityProperty("BOD")
    BOD.hasName.append("Biochemical Oxygen Demand")
    BOD.hasDescription.append(
        "BOD (Biochemical Oxygen Demand) water measurement is a method used to determine the amount of oxygen consumed by microorganisms as they break down organic matter in water. It is a measure of the amount of organic pollution present in the water and is often used to monitor the quality of surface water and wastewater. The BOD measurement is important in determining the health of the aquatic ecosystem and ensuring that the water is safe for human use.")
    BODMeasurement.isMeasuredIn.append(mlperLitter)
    BODMeasurement.relatesToProperty.append(BOD)
    trialTestInfrastructure1.hasMeasurement.append(BODMeasurement)

    KS4_3Measurement = saref.Measurement("KS4_3Measurement")
    CalciumCarbonate = saref4water.AcceptabilityProperty("CalciumCarbonate")
    CalciumCarbonate.hasName.append("Calcium Carbonate")
    CalciumCarbonate.hasDescription.append(
        "A common mineral that is found in many natural settings and is also a major component of many construction materials, such as cement and limestone. It is a white, odorless powder or crystal that occurs naturally in the form of calcite and aragonite. Calcium carbonate is widely used as a filler in the manufacture of papers, paints, and plastics, and is also used in the production of lime, which is used in agriculture, construction, and chemical industries. In water treatment plants, it is used to reduce water acidity and to remove impurities. It is also used as a dietary supplement for calcium and as an antacid.")
    KS4_3Measurement.isMeasuredIn.append(mlperLitter)
    KS4_3Measurement.relatesToProperty.append(CalciumCarbonate)
    trialTestInfrastructure1.hasMeasurement.append(KS4_3Measurement)

    KS8_2Measurement = saref.Measurement("KS8_2Measurement")
    AcidCapacity = saref4water.AcceptabilityProperty("AcidCapacity")
    AcidCapacity.hasName.append("Acid Capacity")
    AcidCapacity.hasDescription.append(
        "Acid Capacity")
    KS8_2Measurement.isMeasuredIn.append(mlperLitter)
    KS8_2Measurement.relatesToProperty.append(AcidCapacity)
    trialTestInfrastructure1.hasMeasurement.append(KS8_2Measurement)

    TSSMeasurement = saref.Measurement("TSSMeasurement")
    TSSMeasurement.isMeasuredIn.append(mlperLitter)
    TSSMeasurement.relatesToProperty.append(saref4water.TotalDissolvedSolids)
    trialTestInfrastructure1.hasMeasurement.append(TSSMeasurement)

    PhosphorousMeasurement = saref.Measurement("PhosphorousMeasurement")
    Phosphorous = saref4water.ChemicalProperty("Phosphorous")
    Phosphorous.hasName.append("Phosphorous")
    Phosphorous.hasDescription.append(
        "PO4-P stands for phosphorus in the form of orthophosphate. It is a measure of the amount of phosphorous in water, which can be an indicator of water quality. High levels of PO4-P can lead to excessive growth of algae and other aquatic plants, which can harm the ecosystem and make the water unsafe for swimming and other activities.")
    PhosphorousMeasurement.isMeasuredIn.append(mlperLitter)
    PhosphorousMeasurement.relatesToProperty.append(Phosphorous)
    trialTestInfrastructure1.hasMeasurement.append(PhosphorousMeasurement)

    OrthophosphateMeasurement = saref.Measurement("OrthophosphateMeasurement")
    Orthophosphate = saref4water.ChemicalProperty("Orthophosphate")
    Orthophosphate.hasName.append("Orthophosphate")
    Orthophosphate.hasDescription.append(
        "oPO4 stands for orthophosphate. It is a form of inorganic phosphorous that is commonly found in natural water sources. It is an important nutrient for plants and can be used as a fertilizer. However, excessive levels of oPO4 in water can lead to eutrophication, a process where an overabundance of nutrients leads to excessive growth of algae and other aquatic plants, which can harm the ecosystem and make the water unsafe for swimming and other activities.")
    OrthophosphateMeasurement.isMeasuredIn.append(mlperLitter)
    OrthophosphateMeasurement.relatesToProperty.append(Orthophosphate)
    trialTestInfrastructure1.hasMeasurement.append(OrthophosphateMeasurement)

    TotalPhosphorousMeasurement = saref.Measurement("PhosphorousMeasurement")
    Phosphorous = saref4water.ChemicalProperty("Phosphorous")
    Phosphorous.hasName.append("Phosphorous")
    Phosphorous.hasDescription.append(
        "PO4-P stands for phosphorus in the form of orthophosphate. It is a measure of the amount of phosphorous in water, which can be an indicator of water quality. High levels of PO4-P can lead to excessive growth of algae and other aquatic plants, which can harm the ecosystem and make the water unsafe for swimming and other activities.")
    TotalPhosphorousMeasurement.isMeasuredIn.append(mlperLitter)
    TotalPhosphorousMeasurement.relatesToProperty.append(Phosphorous)
    trialTestInfrastructure1.hasMeasurement.append(TotalPhosphorousMeasurement)

    ZincMeasurement = saref.Measurement("ZincMeasurement")
    ZincMeasurement.isMeasuredIn.append(mlperLitter)
    Zinc = saref4water.ChemicalProperty("Zinc")
    Zinc.hasName.append("Zinc")
    Zinc.hasDescription.append("Zinc")
    ZincMeasurement.relatesToProperty.append(Zinc)
    trialTestInfrastructure1.hasMeasurement.append(ZincMeasurement)

    PotasiumMeasurement = saref.Measurement("PotasiumMeasurement")
    Potasium = saref4water.ChemicalProperty("Potasium")
    Potasium.hasName.append("Potasium")
    Potasium.hasDescription.append('''
        Potassium is a chemical element with the symbol K (from Neo-Latin kalium) and atomic number 19. It was first isolated from potash, the ashes of plants, from which its name derives. In the periodic table, potassium is one of the alkali metals. All of the alkali metals have a single valence electron in the outer electron shell, which is easily removed to create an ion with a positive charge – a cation, that combines with anions to form salts. 
    ''')
    PotasiumMeasurement.isMeasuredIn.append(mlperLitter)
    PotasiumMeasurement.relatesToProperty.append(Potasium)
    trialTestInfrastructure1.hasMeasurement.append(PotasiumMeasurement)

    SodiumMeasurement = saref.Measurement("SodiumMeasurement")
    SodiumMeasurement.isMeasuredIn.append(mlperLitter)
    SodiumMeasurement.relatesToProperty.append(saref4water.Sodium)
    trialTestInfrastructure1.hasMeasurement.append(SodiumMeasurement)

    ClorineMeasurement = saref.Measurement("ChlorineMeasurement")
    Chlorine = saref4water.ChemicalProperty("Chlorine")
    Chlorine.hasName.append("Chlorine")
    Chlorine.hasDescription.append('''
        Chlorine is a chemical element with the symbol Cl and atomic number 17. It is a halogen, a highly reactive, yellow-green gas at room temperature and pressure. Chlorine is a powerful oxidizing agent, meaning it readily gains electrons from other atoms or molecules, making them more reactive. Because of this, chlorine is widely used as a disinfectant, bleach and water treatment chemical. Chlorine is also used in the production of many industrial and consumer products, such as PVC plastic, and numerous drugs and pesticides. Chlorine is toxic to humans and animals in high concentrations, and can cause respiratory problems.
    ''')
    ClorineMeasurement.isMeasuredIn.append(mlperLitter)
    ClorineMeasurement.relatesToProperty.append(Chlorine)
    trialTestInfrastructure1.hasMeasurement.append(ClorineMeasurement)

    DisolvedIronMeasurement = saref.Measurement("DisolvedIronMeasurement")
    DissChlorine = saref4water.ChemicalProperty("DissolvedChlorine")
    DissChlorine.hasName.append("Dissolved Chlorine")
    DissChlorine.hasDescription.append('''
        Iron in the form of Fe2+ or Fe3+ ions can occur dissolved in water and is called ferrous or ferric iron, respectively. In natural water systems, iron can occur in both dissolved and solid forms, and the amount and form of iron present can vary depending on the pH and redox conditions of the water. Iron is an essential nutrient for many organisms, but high levels of dissolved iron can also have negative effects on water quality and can cause staining and discoloration of surfaces.
        ''')
    DisolvedIronMeasurement.isMeasuredIn.append(mlperLitter)
    DisolvedIronMeasurement.relatesToProperty.append(DissChlorine)
    trialTestInfrastructure1.hasMeasurement.append(DisolvedIronMeasurement)

    CalciumMagneseMeasurement = saref.Measurement("CalciumMagneseMeasurement")
    CaMgProperty = saref4water.ChemicalProperty("CaMgProperty")
    CaMgProperty.hasName.append("Dissolved CaMgProperty")
    CalciumMagneseMeasurement.isMeasuredIn.append(mlperLitter)
    CalciumMagneseMeasurement.relatesToProperty.append(CaMgProperty)
    trialTestInfrastructure1.hasMeasurement.append(CalciumMagneseMeasurement)

    CalciumMeasurement = saref.Measurement("CalciumMeasurement")
    Calcium = saref4water.ChemicalProperty("Calcium")
    Calcium.hasName.append("Calcium")
    Calcium.hasDescription.append('''
        Calcium in water refers to the presence of calcium ions (Ca2+) dissolved in water. Calcium is a common mineral found in natural water sources, such as lakes, rivers, and groundwater. The amount of calcium present in water is measured in parts per million (ppm) or milligrams per liter (mg/L).
    ''')
    CalciumMeasurement.isMeasuredIn.append(mlperLitter)
    CalciumMeasurement.relatesToProperty.append(Calcium)
    trialTestInfrastructure1.hasMeasurement.append(CalciumMeasurement)

    BariumMeasurement = saref.Measurement("BariumMeasurement")
    Barium = saref4water.ChemicalProperty("Barium")
    Barium.hasName.append("Barium")
    Barium.hasDescription.append('''
        Barium is a chemical element with the symbol Ba and atomic number 56. It is a soft, silvery-white metal that belongs to the alkaline earth elements group in the periodic table. Barium is not found as a free element in nature, but instead occurs as minerals such as barite and witherite. Barium is reactive and does not occur naturally in its elemental form. Barium compounds have a variety of applications, such as in the production of glass and ceramics, as a drilling fluid in oil and gas exploration, and in the manufacture of certain types of fireworks to produce green flames. Barium compounds are also used in medicine, for example, as a contrast agent in X-ray imaging. Barium is toxic in large amounts and should be handled with care.
        ''')
    BariumMeasurement.isMeasuredIn.append(mlperLitter)
    BariumMeasurement.relatesToProperty.append(Barium)
    trialTestInfrastructure1.hasMeasurement.append(BariumMeasurement)

    ManganeseMeasurement = saref.Measurement("ManganeseMeasurement")
    ManganeseMeasurement.isMeasuredIn.append(mlperLitter)
    ManganeseMeasurement.relatesToProperty.append(saref4water.Manganese)
    trialTestInfrastructure1.hasMeasurement.append(ManganeseMeasurement)

    CopperMeasurement = saref.Measurement("CopperMeasurement")
    CopperMeasurement.isMeasuredIn.append(mlperLitter)
    CopperMeasurement.relatesToProperty.append(saref4water.Copper)
    trialTestInfrastructure1.hasMeasurement.append(CopperMeasurement)

    SyliconDioxideMeasurement = saref.Measurement("SyliconDioxideMeasurement")
    SyliconDioxide = saref4water.ChemicalProperty("SyliconDioxide")
    SyliconDioxide.hasName.append("Sylicon Dioxide")
    SyliconDioxide.hasDescription.append('''
        chemical compound composed of one silicon atom and two oxygen atoms. It is a common mineral found in many types of rocks, including sand, quartz, and granite. It is also found in many other natural materials such as diatomaceous earth, and is a major component of many man-made materials, including glass and ceramics. It is an important material in many industrial and technological applications, including as a filler and abrasive in products such as toothpaste and sandpaper.
    ''')
    SyliconDioxideMeasurement.isMeasuredIn.append(mlperLitter)
    SyliconDioxideMeasurement.relatesToProperty.append(saref4water.Copper)
    trialTestInfrastructure1.hasMeasurement.append(SyliconDioxideMeasurement)

    AmoniumMeasurement = saref.Measurement("AmoniumMeasurement")
    AmoniumMeasurement.isMeasuredIn.append(mlperLitter)
    AmoniumMeasurement.relatesToProperty.append(saref4water.Ammonium)
    trialTestInfrastructure1.hasMeasurement.append(AmoniumMeasurement)

    NitriteMeasurement = saref.Measurement("NitriteMeasurement")
    NitriteMeasurement.isMeasuredIn.append(mlperLitter)
    NitriteMeasurement.relatesToProperty.append(saref4water.Nitrite)
    trialTestInfrastructure1.hasMeasurement.append(NitriteMeasurement)

    TotalNitrogenMeasurement = saref.Measurement("TotalNitrogenMeasurement")
    TotalNitrogen = saref4water.ChemicalProperty("TotalNitrogen")
    TotalNitrogen.hasName.append("Total Nitrogen")
    TotalNitrogen.hasDescription.append('''
         Total Nitrogen, it is a measure of the combined concentration of all forms of nitrogen (NH4+, NO2-, NO3-) present in a water or soil sample. It is an important parameter used to monitor water and soil quality, as well as to assess the level of pollution by nitrogen compounds. In water, high levels of TN can lead to eutrophication and can harm aquatic life. In soil, it can be used as an indicator of the fertility of the soil and the availability of nitrogen for plant growth. The TN measurement provides an overall picture of the total amount of nitrogen present in a sample, rather than focusing on individual forms of nitrogen.
    ''')
    TotalNitrogenMeasurement.isMeasuredIn.append(mlperLitter)
    TotalNitrogenMeasurement.relatesToProperty.append(TotalNitrogen)
    trialTestInfrastructure1.hasMeasurement.append(TotalNitrogenMeasurement)

    SulphateMeasurement = saref.Measurement("SulphateMeasurement")
    SulphateMeasurement.isMeasuredIn.append(mlperLitter)
    SulphateMeasurement.relatesToProperty.append(saref4water.Sulphate)
    trialTestInfrastructure1.hasMeasurement.append(SulphateMeasurement)

    AdsorbableOrganicHalidesMeasurement = saref.Measurement("AdsorbableOrganicHalidesMeasurement")
    AdsorbableOrganicHalides = saref4water.ChemicalProperty("AdsorbableOrganicHalides")
    AdsorbableOrganicHalides.hasName.append("Adsorbable Organic Halides")
    AdsorbableOrganicHalides.hasDescription.append('''
        AOX stands for Adsorbable Organic Halides, it is a measure of the halogenated organic compounds present in a water or waste stream. The halogens (chlorine, bromine, and iodine) are added to many organic compounds to make them more resistant to degradation and to increase their usefulness in industrial applications. AOX is a measure of the total halogen content in organic compounds that are adsorbable on activated carbon. Some examples of AOX include chlorinated pesticides, polychlorinated biphenyls (PCBs), and polychlorinated dibenzo-p-dioxins and dibenzofurans (PCDD/PCDFs). High levels of AOX in water and waste streams can be harmful to aquatic life and can be an indicator of industrial pollution. It is regulated in some countries to reduce the environmental impact of these compounds.
    ''')
    AdsorbableOrganicHalidesMeasurement.isMeasuredIn.append(mlperLitter)
    AdsorbableOrganicHalidesMeasurement.relatesToProperty.append(AdsorbableOrganicHalides)
    trialTestInfrastructure1.hasMeasurement.append(AdsorbableOrganicHalidesMeasurement)

    BenzotriazoleMeasurement = saref.Measurement("BenzotriazoleMeasurement")
    Benzotriazole = saref4water.ChemicalProperty("Benzotriazole")
    Benzotriazole.hasName.append("Benzotriazole")
    Benzotriazole.hasDescription.append('''
        Benzotriazole (BTA) is an organic chemical compound with the chemical formula C6H5N3. It is a colorless solid that is soluble in water. Benzotriazole is used as a corrosion inhibitor, a scale inhibitor and a chelating agent. It is commonly used in industrial water treatment, particularly in the cooling systems of power plants and in the oil and gas industry to prevent corrosion in pipelines and equipment. It is also used in the paper industry as a dispersant and in the textile industry as a dye leveling agent.
    ''')
    BenzotriazoleMeasurement.isMeasuredIn.append(mlperLitter)
    BenzotriazoleMeasurement.relatesToProperty.append(Benzotriazole)
    trialTestInfrastructure1.hasMeasurement.append(BenzotriazoleMeasurement)

    return wsisSchema

def CS2_Solvay(wsisSchema):
    saref4water = get_namespace("https://saref.etsi.org/saref4watr/")
    saref = get_namespace("https://saref.etsi.org/core/")
    om = get_namespace("http://www.ontology-of-units-of-measure.org/resource/om-2/")

    mlperLitter = om.PrefixedGramPerLitre("milligramPerLitre")

    solvay = wsisSchema.Industry("SolvayAretusa")
    solvay.hasName.append("Solvay-Aretusa")
    solvay.hasDescription.append('''
        The Rosignano Solvay chemical industry is one of the oldest and largest chemical plants in Italy: it produces sodium carbonate, bicarbonate (also for pharmaceutical use), calcium chloride, chlorine, hydrochloric acid, chloromethane, plastic materials, peracetic acid and hydrogen peroxide, which require a high amount of water and strict management for all the production steps.
    ''')
    solvay.hasOwner.append("Rosignano Solvay chemical ")

    RosignanoSolvayPeroxideTreatmentPlant  = wsisSchema.Technology("RosignanoSolvayPeroxideTreatmentPlant")
    RosignanoSolvayPeroxideTreatmentPlant.hasName.append("Rosignano Solvay Peroxide Treatment Plant")
    RosignanoSolvayPeroxideTreatmentPlant.hasDescription.append("Rosignano Solvay Peroxide Treatment Plant configuration")
    solvay.usesTechnology.append(RosignanoSolvayPeroxideTreatmentPlant)

    ASAWWTP = wsisSchema.Technology("ASAWWTP")
    ASAWWTP.hasName.append("ASA Waste-Water Treatment Plant")
    RosignanoSolvayPeroxideTreatmentPlant.usesTechnology.append(ASAWWTP)

    WasteWaterASA = saref4water.Water("WasteWaterASA")
    RosignanoSolvayPeroxideTreatmentPlant.canProcess.append(WasteWaterASA)
    waterWRPAretusa = saref4water.Water("waterWRTAretusa")
    RosignanoSolvayPeroxideTreatmentPlant.generates.append(waterWRPAretusa)

    SolvayCoolingTowers = wsisSchema.Technology("SolvayCoolingTowers")
    SolvayCoolingTowers.hasName.append("Solvay Cooling Towers")
    SolvayCoolingTowers.canProcess.append(waterWRPAretusa)
    waterToWWTP = saref4water.Water("waterToWWTP")
    SolvayCoolingTowers.generates.append(waterToWWTP)
    waterToSea = saref4water.Water("WaterDischargeToSea")
    SolvayCoolingTowers.generates.append(waterToSea)

    FlowRateMeasurement = saref.Measurement("FlowRateMeasurement")
    cubicMetrePerHour = saref.UnitOfMeasure("cubicMetrePerHour")
    cubicMetrePerHour.hasName.append("m^3/h")
    FlowRateMeasurement.isMeasuredIn.append(cubicMetrePerHour)
    FlowRateMeasurement.relatesToProperty.append(saref4water.FlowRate)
    WasteWaterASA.hasMeasurement.append(FlowRateMeasurement)


    phMeasurement = saref.Measurement("phMeasurement")
    ph = saref4water.AcceptabilityProperty("ph")
    ph.hasName.append("pH")
    ph.hasDescription.append("Quantitative measure of the acidity or basicity of aqueous or other liquid solutions")
    phMeasurement.relatesToProperty.append(ph)
    WasteWaterASA.hasMeasurement.append(phMeasurement)

    TOCMeasurement= saref.Measurement("TOCMeasurement")
    TOC = saref4water.AcceptabilityProperty("TotalOrganicCarbon")
    TOC.hasName.append("Total Organic Carbon")
    TOCMeasurement.isMeasuredIn.append(mlperLitter)
    TOCMeasurement.relatesToProperty.append(TOC)
    WasteWaterASA.hasMeasurement.append(TOCMeasurement)

    CODMeasurement = saref.Measurement("CODMeasurement")
    totalCOD = saref4water.AcceptabilityProperty("COD")
    totalCOD.hasName.append("Chemical Oxigen Demand")
    totalCOD.hasDescription.append(
        "The COD is the estimate of oxygen required for the portion of organic matter in wastewater that is subjected to oxidation and also the amount of oxygen consumed by organic matter from boiling acid potassium dichromate solution.")
    CODMeasurement.relatesToProperty.append(totalCOD)
    CODMeasurement.isMeasuredIn.append(mlperLitter)
    WasteWaterASA.hasMeasurement.append(CODMeasurement)

    NO3Measurment = saref.Measurement("NO3Measurment")
    NO3Measurment.isMeasuredIn.append(mlperLitter)
    NO3Measurment.relatesToProperty.append(saref4water.Nitrate)
    WasteWaterASA.hasMeasurement.append(NO3Measurment)

    SulfateMeasurement = saref.Measurement("SulfateMeasurement")
    Sulfate = saref4water.ChemicalProperty("Sulfate")
    Sulfate.hasName.append("Sulfate")
    Sulfate.hasDescription.append("a chemical formed from sulphur, oxygen, and another element")
    SulfateMeasurement.isMeasuredIn.append(mlperLitter)
    SulfateMeasurement.relatesToProperty.append(Sulfate)
    WasteWaterASA.hasMeasurement.append(SulfateMeasurement)

    HidrogenPeroxideMeasurement = saref.Measurement("HidrogenPeroxideMeasurement")
    HidrogenPeroxide = saref4water.ChemicalProperty("HidrogenPeroxide")
    HidrogenPeroxide.hasName.append("HidrogenPeroxide")
    HidrogenPeroxide.hasDescription.append("""
      H2O2 refers to hydrogen peroxide, a chemical compound made up of two hydrogen atoms and two oxygen atoms. It is a clear liquid that is a powerful oxidizer and is commonly used as a disinfectant, bleaching agent, and an oxidizer. It is used in many households as a cleaning agent and as a treatment for minor cuts and scrapes. In higher concentrations, it can be used as rocket propellant, in hair dyes and in some industrial process. It's important to handle hydrogen peroxide with care as it can be harmful if ingested or if it comes into contact with the eyes or skin.                                     
    """)
    HidrogenPeroxideMeasurement.isMeasuredIn.append(mlperLitter)
    HidrogenPeroxideMeasurement.relatesToProperty.append(Sulfate)
    WasteWaterASA.hasMeasurement.append(HidrogenPeroxideMeasurement)

    AluminiumMeasurement = saref.Measurement("AluminiumMeasurement")
    AluminiumMeasurement.isMeasuredIn.append(mlperLitter)
    AluminiumMeasurement.relatesToProperty.append(saref4water.Aluminium)
    WasteWaterASA.hasMeasurement.append(AluminiumMeasurement)

    IronMeasurement = saref.Measurement("IronMeasurement")
    IronMeasurement.isMeasuredIn.append(mlperLitter)
    IronMeasurement.relatesToProperty.append(saref4water.Aluminium)
    WasteWaterASA.hasMeasurement.append(IronMeasurement)

    SolvayCoolingTowers.hasMeasurement.append(phMeasurement)
    SolvayCoolingTowers.hasMeasurement.append(CODMeasurement)
    SolvayCoolingTowers.hasMeasurement.append(NO3Measurment)
    SolvayCoolingTowers.hasMeasurement.append(SulfateMeasurement)
    SolvayCoolingTowers.hasMeasurement.append(AluminiumMeasurement)
    SolvayCoolingTowers.hasMeasurement.append(IronMeasurement)

    return wsisSchema

def CS3_AntwerpHarbour (wsisSchema):
    saref4water = get_namespace("https://saref.etsi.org/saref4watr/")
    saref = get_namespace("https://saref.etsi.org/core/")
    om = get_namespace("http://www.ontology-of-units-of-measure.org/resource/om-2/")
    aq= get_namespace("")

    mlperLitter = om.PrefixedGramPerLitre("milligramPerLitre")

    AntwerpHarbour = wsisSchema.Industry("AntwerpHarbour")
    AntwerpHarbour.hasName.append("Antwerp-Harbour")
    AntwerpHarbour.hasDescription.append('''
        The Port of Antwerp is the leading European petrochemical and chemical cluster in Europe and home to key industrial players in chemicals production. Several of these chemical companies are large water users that require water for processing products, cooling, and steam production. The freshwater source that connects to the Antwerp harbour is the Albert Canal. The Albert Canal on its turn receives water from the river Meuse. Freshwater of the river Meuse transported through the Albert Canal plays a key role in the Flanders’ navigation transport and water use for economic activities. Water is transported from the river Meuse towards the Antwerp harbour through shipping transport and sluice activities. Drinking water company Water-link abstracts water from the Albert Canal for drinking water production.
    ''')
    AntwerpHarbour.hasOwner.append("Port of Antwerp")

    AlbertCanal = wsisSchema.Technology("AlbertCanal")
    AlbertCanal.hasName.append("Albert Canal")
    AlbertCanal.hasDescription.append(
        "Albert Canal")


    TemperatureMeasurement = saref.Measurement("TemperatureMeasurement")
    TemperatureMeasurement.isMeasuredIn.append(om.centidegreeCelsius)
    TemperatureMeasurement.relatesToProperty.append(saref4water.FlowTemperature)

    ConductivityMeasurement = saref.Measurement("ConductivityMeasurement")
    microSiemmensPerCm = saref.UnitOfMeasure("microSiemmensPerCm")
    microSiemmensPerCm.hasName.append("\u03BCS/cm")
    ConductivityMeasurement.isMeasuredIn.append(microSiemmensPerCm)
    ConductivityMeasurement.relatesToProperty.append(saref4water.Conductivity)

    WaterLevelMeasurement = saref.Measurement("WaterLevelMeasurement")
    mTAW = saref.UnitOfMeasure("mTAW")
    mTAW.hasName.append("mTAW")
    WaterLevelMeasurement.isMeasuredIn.append(mTAW)
    waterLevel = saref4water.ChemicalProperty("waterLevel")
    waterLevel.hasName.append("waterLevel")
    waterLevel.hasDescription.append('''
        Water level refers to the height of the water surface in relation to a reference point, such as sea level or a fixed point on a shoreline. Water levels can change due to a variety of factors, including tides, weather, and human activities. The measurement of water level is important for many activities such as navigation, flood control, and monitoring of water resources. There are different ways to measure water level, such as using a staff gauge, a pressure transducer or a radar sensor, depending on the location, the precision and the frequency of measurements required.
        ''')
    WaterLevelMeasurement.relatesToProperty.append(waterLevel)

    MeasurementStation1 = wsisSchema.Device("MeasurementStation#M1")
    MeasurementStation1.hasName.append("MonitoringStation_1")
    MeasurementStation1.id.append(str("https://cs3.rtm.aquaspice.eurecatprojects.com/broker/ngsi-ld/v1/entities?id=urn:ngsi-ld:AquaSpice:measurementStation:North"))
    MeasurementStation1.makesMeasurement.append(TemperatureMeasurement)
    MeasurementStation1.makesMeasurement.append(ConductivityMeasurement)
    MeasurementStation1.makesMeasurement.append(WaterLevelMeasurement)

    WaterPortToCanal = saref4water.Water("WaterPortToCanal")
    AntwerpHarbour.generates.append(WaterPortToCanal)
    AlbertCanal.canProcess.append(WaterPortToCanal)
    AlbertCanalWater = saref4water.Water("AlbertCanalWater")
    AlbertCanal.generates.append(AlbertCanalWater)

    UpstreamAreaAlbertCanal = wsisSchema.Technology("UpstreamAreaAlbertCanal")
    UpstreamAreaAlbertCanal.canProcess.append(AlbertCanalWater)



    return wsisSchema

def CS3_BASF(wsisSchema):
    saref4water = get_namespace("https://saref.etsi.org/saref4watr/")
    saref = get_namespace("https://saref.etsi.org/core/")
    om = get_namespace("http://www.ontology-of-units-of-measure.org/resource/om-2/")

    mlperLitter = om.PrefixedGramPerLitre("milligramPerLitre")

    BASF = wsisSchema.Industry("BASF")
    BASF.hasName.append("BASF")
    BASF.hasDescription.append('''
        BASF utilities operate internal grids where cooling water is exchanged between production plants and cooling towers. The BASF cooling water system is based on a so-called half open/half closed loop where fresh water is pumped out of the harbour dock B3.
       ''')
    BASF.hasOwner.append("Port of Antwerp")


    GAC_1 = wsisSchema.Technology("GAC_1")
    GAC_1.hasName.append("GAC_1")
    waterNTBA = saref4water.Water("waterNTBA")
    GAC_1.canProcess.append(waterNTBA)
    Q1811 = saref4water.Water("Q1811")
    GAC_1.canProcess.append(Q1811)
    waterGAC_1 = saref4water.Water("waterGAC_1")
    GAC_1.generates.append(waterGAC_1)
    BASF.usesTechnology.append(GAC_1)

    UF_1 = wsisSchema.Technology("GAC_1")
    UF_1.hasName.append("UF-1")
    UF_1.canProcess.append(waterGAC_1)
    waterUF1= saref4water.Water("waterUF1")
    UF_1.generates.append(waterUF1)

    RO_1 = wsisSchema.Technology("RO_1")
    RO_1.hasName.append("RO-1")
    RO_1.canProcess.append(waterUF1)
    sprayWater = saref4water.Water("sprayWater")
    WaterRO1 = saref4water.Water("WaterRO1")
    RO_1.generates.append(sprayWater)
    RO_1.generates.append(WaterRO1)

    SCAV_1 = wsisSchema.Technology("SCAV_1")
    SCAV_1.hasName.append("SCAV_1")
    SCAV_1.canProcess.append(Q1811)
    waterSCAV1= saref4water.Water("waterSCAV1")
    SCAV_1.generates.append(waterSCAV1)

    SAC_1 = wsisSchema.Technology("SAC_1")
    SAC_1.hasName.append("SAC_1")
    SAC_1.canProcess.append(Q1811)
    SAC_1.canProcess.append(waterSCAV1)
    waterSAC1 = saref4water.Water("WaterSAC1")
    SAC_1.generates.append(waterSAC1)

    DEG1 = wsisSchema.Technology("DEG1")
    DEG1.hasName.append("DEG1")
    DEG1.canProcess.append(waterSAC1)
    waterDEG1 = saref4water.Water("waterDEG1")
    DEG1.generates.append(waterDEG1)

    SBA_1 = wsisSchema.Technology("SBA_1")
    SBA_1.hasName.append("SBA_1")
    SBA_1.canProcess.append(waterDEG1)
    waterSBA1= saref4water.Water("waterSBA1")
    SBA_1.generates.append(waterSBA1)

    MB_1 = wsisSchema.Technology("MB_1")
    MB_1.hasName.append("MB_1")
    MB_1.canProcess.append(WaterRO1)
    MB_1.canProcess.append(SBA_1)
    BoiledFeedWater_1 = saref4water.Water("BoiledFeedWater_1")
    MB_1.generates.append(BoiledFeedWater_1)

    StreamBlowDown = saref4water.Water("StreamBlowDown")
    EDI1 = wsisSchema.Technology("EDI1")
    EDI1.hasName.append("EDI1")
    EDI1.canProcess.append(StreamBlowDown)
    EDI1.generates.append(BoiledFeedWater_1)

    FlowRateMeasurement = saref.Measurement("FlowRateMeasurement")
    cubicMetrePerHour = saref.UnitOfMeasure("cubicMetrePerHour")
    cubicMetrePerHour.hasName.append("m^3/h")
    FlowRateMeasurement.isMeasuredIn.append(cubicMetrePerHour)
    FlowRateMeasurement.relatesToProperty.append(saref4water.FlowRate)
    RO_1.hasMeasurement.append(FlowRateMeasurement)

    TemperatureMeasurement = saref.Measurement("TemperatureMeasurement")
    TemperatureMeasurement.isMeasuredIn.append(om.centidegreeCelsius)
    TemperatureMeasurement.relatesToProperty.append(saref4water.FlowTemperature)
    RO_1.hasMeasurement.append(TemperatureMeasurement)

    TOCMeasurement = saref.Measurement("TOCMeasurement")
    TOC = saref4water.AcceptabilityProperty("TotalOrganicCarbon")
    TOC.hasName.append("Total Organic Carbon")
    TOCMeasurement.isMeasuredIn.append(mlperLitter)
    TOCMeasurement.relatesToProperty.append(TOC)
    RO_1.hasMeasurement.append(TOCMeasurement)

    phMeasurement = saref.Measurement("phMeasurement")
    ph = saref4water.AcceptabilityProperty("ph")
    ph.hasName.append("pH")
    ph.hasDescription.append("Quantitative measure of the acidity or basicity of aqueous or other liquid solutions")
    phMeasurement.relatesToProperty.append(ph)
    RO_1.hasMeasurement.append(phMeasurement)

    ConductivityMeasurement = saref.Measurement("ConductivityMeasurement")
    microSiemmensPerCm = saref.UnitOfMeasure("microSiemmensPerCm")
    microSiemmensPerCm.hasName.append("\u03BCS/cm")
    ConductivityMeasurement.isMeasuredIn.append(microSiemmensPerCm)
    ConductivityMeasurement.relatesToProperty.append(saref4water.Conductivity)
    RO_1.hasMeasurement.append(ConductivityMeasurement)

    TurbidityMeasurement = saref.Measurement("TurbidityMeasurement")
    FTU = saref.UnitOfMeasure("FTU")
    FTU.hasName.append("Formazine Turbidity Unit")
    FTU.hasDescription.append(
        "FTU became the defined unit of measurement after the acceptance of Formazine as the primary reference standard for turbidity. FTU, as well as any measurement unit derived from, or that references FTU does not specify how a device measures turbidity in a water sample")
    TurbidityMeasurement.isMeasuredIn.append(FTU)
    TurbidityMeasurement.relatesToProperty.append(saref4water.Turbidity)
    RO_1.hasMeasurement.append(TurbidityMeasurement)

    PhosphateMeasurement = saref.Measurement("PhosphateMeasurement")
    Phosphate =saref4water.ChemicalProperty("Phosphate")
    Phosphate.hasName.append("Phosphate")
    Phosphate.hasDescription.append("A phosphate is an anion, salt, functional group or ester derived from a phosphoric acid.")
    PhosphateMeasurement.isMeasuredIn.append(mlperLitter)
    PhosphateMeasurement.relatesToProperty.append(Phosphate)
    RO_1.hasMeasurement.append(PhosphateMeasurement)

    ChlorideMeasurement = saref.Measurement("ChlorideMeasurement")
    ChlorideMeasurement.isMeasuredIn.append(mlperLitter)
    ChlorideMeasurement.relatesToProperty.append(saref4water.Chloride)
    RO_1.hasMeasurement.append(ChlorideMeasurement)

    IronMeasurement = saref.Measurement("IronMeasurement")
    IronMeasurement.isMeasuredIn.append(mlperLitter)
    IronMeasurement.relatesToProperty.append(saref4water.Iron)
    RO_1.hasMeasurement.append(IronMeasurement)

    CalciumMeasurement = saref.Measurement("CalciumMeasurement")
    CalciumMeasurement.isMeasuredIn.append(mlperLitter)
    CalciumMeasurement.relatesToProperty.append(saref4water.Cadmium)
    RO_1.hasMeasurement.append(CalciumMeasurement)

    MagnesiumMeasurement = saref.Measurement("MagnesiumMeasurement")
    Magnesium = saref4water.ChemicalProperty("Magnesium")
    Magnesium.hasName.append("Magnesium")
    Magnesium.hasDescription.append(
        "the chemical element of atomic number 12, a silver-white metal of the alkaline earth series. It is used to make strong lightweight alloys, and is also used in flash bulbs and pyrotechnics, as it burns with a brilliant white flame.")
    MagnesiumMeasurement.isMeasuredIn.append(mlperLitter)
    MagnesiumMeasurement.relatesToProperty.append(Magnesium)
    RO_1.hasMeasurement.append(MagnesiumMeasurement)

    AluminiumMeasurement = saref.Measurement("AluminiumMeasurement")
    AluminiumMeasurement.isMeasuredIn.append(mlperLitter)
    AluminiumMeasurement.relatesToProperty.append(saref4water.Aluminium)
    RO_1.hasMeasurement.append(AluminiumMeasurement)

    PotasiumMeasurement = saref.Measurement("PotasiumMeasurement")
    Potasium = saref4water.ChemicalProperty("Potasium")
    Potasium.hasName.append("Potasium")
    Potasium.hasDescription.append('''
            Potassium is a chemical element with the symbol K (from Neo-Latin kalium) and atomic number 19. It was first isolated from potash, the ashes of plants, from which its name derives. In the periodic table, potassium is one of the alkali metals. All of the alkali metals have a single valence electron in the outer electron shell, which is easily removed to create an ion with a positive charge – a cation, that combines with anions to form salts. 
        ''')
    PotasiumMeasurement.isMeasuredIn.append(mlperLitter)
    PotasiumMeasurement.relatesToProperty.append(Potasium)
    RO_1.hasMeasurement.append(PotasiumMeasurement)

    SodiumMeasurement = saref.Measurement("SodiumMeasurement")
    SodiumMeasurement.isMeasuredIn.append(mlperLitter)
    SodiumMeasurement.relatesToProperty.append(saref4water.Sodium)
    RO_1.hasMeasurement.append(SodiumMeasurement)

    AmoniumMeasurement = saref.Measurement("AmoniumMeasurement")
    AmoniumMeasurement.isMeasuredIn.append(mlperLitter)
    AmoniumMeasurement.relatesToProperty.append(saref4water.Ammonium)
    RO_1.hasMeasurement.append(AmoniumMeasurement)

    NitrogenDioxideMeasurement = saref.Measurement("NitrogenDioxideMeasurement")
    NitrogenDioxideMeasurement.isMeasuredIn.append(mlperLitter)
    NitrogenDioxide = saref4water.ChemicalProperty("NitrogenDioxide")
    NitrogenDioxide.hasName.append("NitrogenDioxide")
    NitrogenDioxide.hasDescription.append('''
        NO2 stands for Nitrogen Dioxide, a toxic gas with the chemical formula NO2. It is a major air pollutant, and exposure to high levels of NO2 can cause respiratory problems and other health issues. It is primarily produced by burning fossil fuels in cars, power plants, and other industrial processes. The European Union and the United States have set limits on the amount of NO2 that can be present in the air to protect public health.
    ''')
    NitrogenDioxideMeasurement.relatesToProperty.append(NitrogenDioxide)
    RO_1.hasMeasurement.append(NitrogenDioxideMeasurement)

    NO3Measurment = saref.Measurement("NO3Measurment")
    NO3Measurment.isMeasuredIn.append(mlperLitter)
    NO3Measurment.relatesToProperty.append(saref4water.Nitrate)
    RO_1.hasMeasurement.append(NO3Measurment)

    TotalNitrogenMeasurement = saref.Measurement("TotalNitrogenMeasurement")
    TotalNitrogen = saref4water.ChemicalProperty("TN")
    TotalNitrogen.hasName.append("Total Nitrogen")
    TotalNitrogen.hasDescription.append(
        "Total Nitrogen is the sum of nitrate (NO3), nitrite (NO2), organic nitrogen and ammonia (all expressed as N). Note that for laboratory analysis purposes, Total")
    TotalNitrogenMeasurement.isMeasuredIn.append(mlperLitter)
    TotalNitrogenMeasurement.relatesToProperty.append(TotalNitrogen)
    RO_1.hasMeasurement.append(TotalNitrogenMeasurement)

    SO4Measurement = saref.Measurement("SO4Measurement")
    SO4Measurement.isMeasuredIn.append(mlperLitter)
    SO4Measurement.relatesToProperty.append(saref4water.Sulphate)
    RO_1.hasMeasurement.append(SO4Measurement)

    return wsisSchema

def CS5_agricola_instances(wsisSchema):
    saref4water= get_namespace("https://saref.etsi.org/saref4watr/")
    saref = get_namespace("https://saref.etsi.org/core/")
    om = get_namespace ("http://www.ontology-of-units-of-measure.org/resource/om-2/")


    agricola = wsisSchema.Industry("AgricolaCaseStudy")
    agricola.hasDescription.append("Agricola SA is a well-known top private meat group of companies located in Bacău County, Romania, which delivers, on a daily basis, approximate 100,000 chickens (more than 150 tonnes of meat). The Group Agricola SA consists of more companies: Agricola Internațional (Fodder production, 4 specialized farms in poultry breeding, 15 chicken farms and a slaughterhouse); Salbac (Cured salamis and boiled/smoked meat products); Europrod (Ready-meals and ready-to-eat products); Avicola Lumina, Constanța county (18 modernized warehouses of laying hens); Aicbac (cereal production for fodders, a small dairy farm and dairy processing unit). Besides, there is also a factory for egg powder production.")
    agricola.hasOwner.append("Agricola Internațional SA")
    agricola.hasName.append("Agricola Demo Site")

    pre_screening1 = wsisSchema.Technology("PreScreening")
    pre_screening1.hasDescription.append("Screening is often used to remove large pieces of waste so that the water can be reused within the processing plant")
    pre_screening1.hasName.append ("Pre-screening")
    agricola.usesTechnology.append(pre_screening1)

    water_operation= saref4water.Water("WaterOperation")
    pre_screening1.canProcess.append(water_operation)

    sludgePreScreening = wsisSchema.SemiSolidMaterial("PreScreeningSludge")
    waterPreScreening = saref4water.Water("WaterPreScreening")
    pre_screening1.generates.append(sludgePreScreening)
    pre_screening1.generates.append(waterPreScreening)

    mixing_tank = wsisSchema.Technology("MixingTank")
    mixing_tank.hasName.append("Mixing Tank")
    pre_screening1.usesTechnology.append(mixing_tank)
    coagulant = wsisSchema.SolidMaterial ("FeCl3")
    flocculant = wsisSchema.SolidMaterial("NaOH")
    mixing_tank.canProcess.append(coagulant)
    mixing_tank.canProcess.append(flocculant)
    mixing_tank.canProcess.append(waterPreScreening)
    waterMixingTank = saref4water.Water("waterGeneratedByMixingTank")
    mixing_tank.generates.append(waterMixingTank)

    DAF = wsisSchema.Technology("DAF")
    DAF.hasName.append("DAF")
    mixing_tank.usesTechnology.append(DAF)
    DAF.canProcess.append(waterMixingTank)
    Air_daf = wsisSchema.Air("AirInDaf")
    DAF.canProcess.append(Air_daf)
    sludgeDAF = wsisSchema.SemiSolidMaterial("sludgeDAF")
    DAF.generates.append(sludgeDAF)
    waterDAF = saref4water.Water("waterDAF")
    DAF.generates.append(waterDAF)

    centralisedTreatment= wsisSchema.Technology("CentralisedTreatment")
    centralisedTreatment.hasName.append("Centralised Treatment Plant")
    DAF.usesTechnology.append(centralisedTreatment)
    centralisedTreatment.canProcess.append(sludgeDAF)
    centralisedTreatment.canProcess.append(waterDAF)

    phMeasurementTest1 = saref.Measurement("phMeasurementTest1")
    ph = saref4water.AcceptabilityProperty("ph")
    ph.hasName.append("pH")
    ph.hasDescription.append("Quantitative measure of the acidity or basicity of aqueous or other liquid solutions")
    phMeasurementTest1.relatesToProperty.append(ph)
    phMeasurementTest1.hasTimestamp.append(datetime.strptime("2022-03-06T21:01:30", '%Y-%m-%dT%H:%M:%S'))
    phMeasurementTest1.hasValue.append(8.48)

    totalCODTest1 = saref.Measurement("TotalCODTest1")
    totalCOD = saref4water.AcceptabilityProperty("totalCOD")
    totalCOD.hasName.append ("total COD")
    totalCOD.hasDescription.append("The COD is the estimate of oxygen required for the portion of organic matter in wastewater that is subjected to oxidation and also the amount of oxygen consumed by organic matter from boiling acid potassium dichromate solution.")

    totalCODTest1.relatesToProperty.append(totalCOD)
    totalCODTest1.hasTimestamp.append(datetime.strptime("2022-03-06T21:01:30", '%Y-%m-%dT%H:%M:%S'))
    totalCODTest1.hasValue.append(126)
    mlperLitter = om.PrefixedGramPerLitre("milligramPerLitre")
    totalCODTest1.isMeasuredIn.append(mlperLitter)

    filteredCODTest1 = saref.Measurement("FilteredCODTest1")
    filteredCOD = saref4water.AcceptabilityProperty("filteredCOD")
    filteredCOD.hasName.append("filtered COD")
    filteredCODTest1.isMeasuredIn.append(mlperLitter)
    filteredCODTest1.relatesToProperty.append(filteredCOD)
    filteredCODTest1.hasTimestamp.append(datetime.strptime("2022-03-06T21:01:30", '%Y-%m-%dT%H:%M:%S'))
    filteredCODTest1.hasValue.append(101)

    BODTest1 = saref.Measurement ("BODTEst1")
    BOD = saref4water.AcceptabilityProperty("BOD")
    BOD.hasName.append("BOD")
    BOD.hasDescription.append("BOD is defined as the amount of dissolved oxygen needed by aerobic biological organisms in a body of water to break down the organic material present in a water sample, at a specific temperature and specified period")
    BODTest1.isMeasuredIn.append(mlperLitter)
    BODTest1.relatesToProperty.append(BOD)
    BODTest1.hasTimestamp.append(datetime.strptime("2022-03-06T21:01:30", '%Y-%m-%dT%H:%M:%S'))
    BODTest1.hasValue.append(44)

    FilteredBODTest1 = saref.Measurement("FilteredBODTEst1")
    FilteredBOD = saref4water.AcceptabilityProperty("FilteredBOD")
    FilteredBOD.hasName.append("Filtered BOD")
    FilteredBODTest1.isMeasuredIn.append(mlperLitter)
    FilteredBODTest1.relatesToProperty.append(FilteredBOD)
    FilteredBODTest1.hasTimestamp.append(datetime.strptime("2022-03-06T21:01:30", '%Y-%m-%dT%H:%M:%S'))
    FilteredBODTest1.hasValue.append(39)

    TOCTEst1 = saref.Measurement("TOCTest1")
    TOC = saref4water.AcceptabilityProperty("TotalOrganicCarbon")
    TOC.hasName.append("Total Organic Carbon")
    TOCTEst1.isMeasuredIn.append(mlperLitter)
    TOCTEst1.relatesToProperty.append(TOC)
    TOCTEst1.hasTimestamp.append(datetime.strptime("2022-03-06T21:01:30", '%Y-%m-%dT%H:%M:%S'))
    TOCTEst1.hasValue.append(20.5)

    TSSTest1 = saref.Measurement("TSSTest1")
    TSSTest1.isMeasuredIn.append(mlperLitter)
    TSSTest1.relatesToProperty.append(saref4water.TotalSuspendedSolids)
    TSSTest1.hasTimestamp.append(datetime.strptime("2022-03-06T21:01:30", '%Y-%m-%dT%H:%M:%S'))
    TSSTest1.hasValue.append(7)

    ISSTest1 = saref.Measurement("ISSTEst1")
    ISS= saref4water.AcceptabilityProperty("ISS")
    ISS.hasName.append("ISS")
    ISS.hasDescription.append("ISS")
    ISSTest1.isMeasuredIn.append(mlperLitter)
    ISSTest1.relatesToProperty.append(ISS)
    ISSTest1.hasTimestamp.append(datetime.strptime("2022-03-06T21:01:30", '%Y-%m-%dT%H:%M:%S'))
    ISSTest1.hasValue.append(1024)

    TurbidityTest1 = saref.Measurement("TurbidityTEst1")
    FTU = saref.UnitOfMeasure("FTU")
    FTU.hasName.append("Formazine Turbidity Unit")
    FTU.hasDescription.append("FTU became the defined unit of measurement after the acceptance of Formazine as the primary reference standard for turbidity. FTU, as well as any measurement unit derived from, or that references FTU does not specify how a device measures turbidity in a water sample")
    TurbidityTest1.isMeasuredIn.append(FTU)
    TurbidityTest1.relatesToProperty.append(saref4water.Turbidity)
    TurbidityTest1.hasTimestamp.append(datetime.strptime("2022-03-06T21:01:30", '%Y-%m-%dT%H:%M:%S'))
    TurbidityTest1.hasValue.append(30)

    TKNTest1 = saref.Measurement("TKNTEst1")
    TKN = saref4water.AcceptabilityProperty("TKN")
    TKN.hasName.append("Total Kjeldahl Nitrogen")
    TKN.hasDescription.append("Total Kjeldahl Nitrogen means the sum of free-ammonia and organic nitrogen compounds, which are converted to ammonium sulfate (NH4)2SO4, under test conditions.")
    TKNTest1.isMeasuredIn.append(mlperLitter)
    TKNTest1.relatesToProperty.append(TKN)
    TKNTest1.hasTimestamp.append(datetime.strptime("2022-03-06T21:01:30", '%Y-%m-%dT%H:%M:%S'))
    TKNTest1.hasValue.append(48.73)

    NH3Test1 = saref.Measurement("NH3Test1")
    Ammonia = saref4water.ChemicalProperty("TKN")
    Ammonia.hasName.append("Ammonia")
    Ammonia.hasDescription.append(
        "Ammonia is an inorganic compound of nitrogen and hydrogen with the formula NH 3.")
    NH3Test1.isMeasuredIn.append(mlperLitter)
    NH3Test1.relatesToProperty.append(Ammonia)
    NH3Test1.hasTimestamp.append(datetime.strptime("2022-03-06T21:01:30", '%Y-%m-%dT%H:%M:%S'))
    NH3Test1.hasValue.append(8.81)

    NH4Test1 = saref.Measurement("NH4Test1")
    AmmoniumCation = saref4water.ChemicalProperty("TKN")
    AmmoniumCation.hasName.append("Ammonium Cation")
    AmmoniumCation.hasDescription.append(
        "The ammonium cation is a positively-charged polyatomic ion with the chemical formula NH+4 or [NH 4] +")
    NH4Test1.isMeasuredIn.append(mlperLitter)
    NH4Test1.relatesToProperty.append(AmmoniumCation)
    NH4Test1.hasTimestamp.append(datetime.strptime("2022-03-06T21:01:30", '%Y-%m-%dT%H:%M:%S'))
    NH4Test1.hasValue.append(9.32)

    NO3Test1 = saref.Measurement("NO3Test1")
    NO3Test1.isMeasuredIn.append(mlperLitter)
    NO3Test1.relatesToProperty.append(saref4water.Nitrate)
    NO3Test1.hasTimestamp.append(datetime.strptime("2022-03-06T21:01:30", '%Y-%m-%dT%H:%M:%S'))
    NO3Test1.hasValue.append(11.8)

    TotalNitrogenTest1 = saref.Measurement("TotalNitrogenTest1")
    TotalNitrogen = saref4water.ChemicalProperty("TN")
    TotalNitrogen.hasName.append("Total Nitrogen")
    TotalNitrogen.hasDescription.append(
        "Total Nitrogen is the sum of nitrate (NO3), nitrite (NO2), organic nitrogen and ammonia (all expressed as N). Note that for laboratory analysis purposes, Total")
    TotalNitrogenTest1.isMeasuredIn.append(mlperLitter)
    TotalNitrogenTest1.relatesToProperty.append(TotalNitrogen)
    TotalNitrogenTest1.hasTimestamp.append(datetime.strptime("2022-03-06T21:01:30", '%Y-%m-%dT%H:%M:%S'))
    TotalNitrogenTest1.hasValue.append(30.4)

    TPTest1 = saref.Measurement("TPTest1")
    TP = saref4water.AcceptabilityProperty("TP")
    TP.hasName.append("TP")
    TP.hasDescription.append("TP")
    TPTest1.isMeasuredIn.append(mlperLitter)
    TPTest1.relatesToProperty.append(TP)
    TPTest1.hasTimestamp.append(datetime.strptime("2022-03-06T21:01:30", '%Y-%m-%dT%H:%M:%S'))
    TPTest1.hasValue.append(1190)

    OPTest1 = saref.Measurement("OPTest1")
    OP = saref4water.ChemicalProperty("Ortho Phosphate")
    OP.hasName.append("OP")
    OP.hasDescription.append("The phosphate or orthophosphate ion [PO4]3−is derived from phosphoric acid by the removal of three protons H+. Removal of one or two protons gives the dihydrogen phosphate ion [H 2PO4]− and the hydrogen phosphate ion [HPO4]2−ion, respectively. These names are also used for salts of those anions, such as ammonium dihydrogen phosphate and trisodium phosphate.")
    OPTest1.isMeasuredIn.append(mlperLitter)
    OPTest1.relatesToProperty.append(OP)
    OPTest1.hasTimestamp.append(datetime.strptime("2022-03-06T21:01:30", '%Y-%m-%dT%H:%M:%S'))
    OPTest1.hasValue.append(3.45)

    TDSTest1 = saref.Measurement("TDSTest1")
    TDSTest1.isMeasuredIn.append(mlperLitter)
    TDSTest1.relatesToProperty.append(saref4water.TotalDissolvedSolids)
    TDSTest1.hasTimestamp.append(datetime.strptime("2022-03-06T21:01:30", '%Y-%m-%dT%H:%M:%S'))
    TDSTest1.hasValue.append(1190)

    AlkalinityTest1 = saref.Measurement("AlkalinityTest1")
    Alkalinity = saref4water.AcceptabilityProperty("Alkalinity")
    Alkalinity.hasName.append("Alkalinity")
    Alkalinity.hasDescription.append("Total alkalinity is measured by collecting a water sample, and measuring the amount of acid needed to bring the sample to a pH of 4.2.")
    AlkalinityTest1.isMeasuredIn.append(mlperLitter)
    AlkalinityTest1.relatesToProperty.append(Alkalinity)
    AlkalinityTest1.hasTimestamp.append(datetime.strptime("2022-03-06T21:01:30", '%Y-%m-%dT%H:%M:%S'))
    AlkalinityTest1.hasValue.append(45)

    FatOilGreaseTest1 = saref.Measurement("FatOilGreaseTest1")
    FatOilGrease = saref4water.AcceptabilityProperty("FatOilGrease")
    FatOilGrease.hasName.append("Fat, Oil, Grease")
    FatOilGrease.hasDescription.append("NMR is a bulk measurement technique which selectively measures all of the oil and fat in the sample regardless of the distribution of the grease")
    FatOilGreaseTest1.isMeasuredIn.append(mlperLitter)
    FatOilGreaseTest1.relatesToProperty.append(FatOilGrease)
    FatOilGreaseTest1.hasTimestamp.append(datetime.strptime("2022-03-06T21:01:30", '%Y-%m-%dT%H:%M:%S'))
    FatOilGreaseTest1.hasValue.append(5.5)

    ConductivityTest1 = saref.Measurement("ConductivityTest1")
    microSiemmensPerCm = saref.UnitOfMeasure("microSiemmensPerCm")
    microSiemmensPerCm.hasName.append("\u03BCS/cm")
    ConductivityTest1.isMeasuredIn.append(mlperLitter)
    ConductivityTest1.relatesToProperty.append(saref4water.Conductivity)
    ConductivityTest1.hasTimestamp.append(datetime.strptime("2022-03-06T21:01:30", '%Y-%m-%dT%H:%M:%S'))
    ConductivityTest1.hasValue.append(1263)

    SO4Test1 = saref.Measurement("So4Test1")
    SO4Test1.isMeasuredIn.append(mlperLitter)
    SO4Test1.relatesToProperty.append(saref4water.Sulphate)
    SO4Test1.hasTimestamp.append(datetime.strptime("2022-03-06T21:01:30", '%Y-%m-%dT%H:%M:%S'))
    SO4Test1.hasValue.append(90.2)

    SilicaSolubleTest1 = saref.Measurement("SilicaSlubleTest1")
    SilicaSoluble = saref4water.ChemicalProperty("SilicaSoluble")
    SilicaSoluble.hasName.append("Silica Soluble")
    SilicaSoluble.hasDescription.append("The silica dissolved and crystallized in the presence of surface seed crystals, ultimately forming a hollow-structured zeolite during crystallization.")
    SilicaSolubleTest1.isMeasuredIn.append(mlperLitter)
    SilicaSolubleTest1.relatesToProperty.append(saref4water.Sulphate)
    SilicaSolubleTest1.hasTimestamp.append(datetime.strptime("2022-03-06T21:01:30", '%Y-%m-%dT%H:%M:%S'))
    SilicaSolubleTest1.hasValue.append('7.80/3.68')

    eColiTest1 = saref.Measurement("eColiTest1")
    MPN_per_100ML = saref.UnitOfMeasure("microSiemmensPerCm")
    MPN_per_100ML.hasName.append("MPN/100ml")
    eColiTest1.isMeasuredIn.append(MPN_per_100ML)
    eColiTest1.relatesToProperty.append(saref4water.EscherichiaColi)
    eColiTest1.hasTimestamp.append(datetime.strptime("2022-03-06T21:01:30", '%Y-%m-%dT%H:%M:%S'))
    eColiTest1.hasValue.append(4800)

    LegionaleaSSPTest1 = saref.Measurement("LegionaleaSSPTest1")
    Legionella = saref4water.BacterialProperty("Legionella")
    Legionella.hasName.append("Legionella")
    Legionella.hasDescription.append("Legionella is a genus of pathogenic gram-negative bacteria that includes the species L. pneumophila, ")
    LegionaleaSSPTest1.isMeasuredIn.append(MPN_per_100ML)
    LegionaleaSSPTest1.relatesToProperty.append(Legionella)
    LegionaleaSSPTest1.hasTimestamp.append(datetime.strptime("2022-03-06T21:01:30", '%Y-%m-%dT%H:%M:%S'))
    LegionaleaSSPTest1.hasValue.append(0)

    CampylobacterSPPTest1 = saref.Measurement("CampylobacterSPPTest1")
    Campylobacter= saref4water.BacterialProperty("Campylobacter")
    Campylobacter.hasName.append("Campylobacter")
    Campylobacter.hasDescription.append("Campylobacter (meaning 'curved bacteria') is a genus of Gram-negative bacteria.")
    CampylobacterSPPTest1.isMeasuredIn.append(MPN_per_100ML)
    CampylobacterSPPTest1.relatesToProperty.append(Legionella)
    CampylobacterSPPTest1.hasTimestamp.append(datetime.strptime("2022-03-06T21:01:30", '%Y-%m-%dT%H:%M:%S'))
    CampylobacterSPPTest1.hasValue.append(0)

    SalmonellaSPPTest1 = saref.Measurement("SalmonellaSPPTest1")
    Salmonella = saref4water.BacterialProperty("Salmonella")
    Salmonella.hasName.append("Salmonella")
    Salmonella.hasDescription.append(
        "Salmonella infection (salmonellosis) is a common bacterial disease that affects the intestinal tract. ")
    SalmonellaSPPTest1.isMeasuredIn.append(MPN_per_100ML)
    SalmonellaSPPTest1.relatesToProperty.append(Legionella)
    SalmonellaSPPTest1.hasTimestamp.append(datetime.strptime("2022-03-06T21:01:30", '%Y-%m-%dT%H:%M:%S'))
    SalmonellaSPPTest1.hasValue.append('Presence')

    PseudomonasSPPTest1 = saref.Measurement("SalmonellaSPPTest1")
    Pseudomonas = saref4water.BacterialProperty("Pseudomonas")
    Pseudomonas.hasName.append("Pseudomonas")
    Pseudomonas.hasDescription.append(
        "Pseudomonas is a genus of Gram-negative, Gammaproteobacteria, belonging to the family Pseudomonadaceae and containing 191 described species ")
    PseudomonasSPPTest1.isMeasuredIn.append(MPN_per_100ML)
    PseudomonasSPPTest1.relatesToProperty.append(Pseudomonas)
    PseudomonasSPPTest1.hasTimestamp.append(datetime.strptime("2022-03-06T21:01:30", '%Y-%m-%dT%H:%M:%S'))
    PseudomonasSPPTest1.hasValue.append(900)

    StaphylococcusAureusTest1 = saref.Measurement("SalmonellaSPPTest1")
    StaphylococcusAureus = saref4water.BacterialProperty("StaphylococcusAureus")
    StaphylococcusAureus.hasName.append("StaphylococcusAureus")
    StaphylococcusAureus.hasDescription.append(
        "Staphylococcus aureus or “staph” is a type of bacteria found on human skin, in the nose, armpit, groin, and other areas. ")
    StaphylococcusAureusTest1.isMeasuredIn.append(MPN_per_100ML)
    StaphylococcusAureusTest1.relatesToProperty.append(StaphylococcusAureus)
    StaphylococcusAureusTest1.hasTimestamp.append(datetime.strptime("2022-03-06T21:01:30", '%Y-%m-%dT%H:%M:%S'))
    StaphylococcusAureusTest1.hasValue.append(280)

    TotalCountTest1 = saref.Measurement("TotalCountTest1")
    TotalCount = saref4water.AcceptabilityProperty("TotalCount")
    TotalCount.hasName.append("Total Count")
    TotalCount.hasDescription.append(
        "Total Count og micro-organims")
    TotalCountTest1.isMeasuredIn.append(MPN_per_100ML)
    TotalCountTest1.relatesToProperty.append(TotalCount)
    TotalCountTest1.hasTimestamp.append(datetime.strptime("2022-03-06T21:01:30", '%Y-%m-%dT%H:%M:%S'))
    TotalCountTest1.hasValue.append(2020000)

    TotalColiformTest1 = saref.Measurement("TotalColiformTest1")
    TotalColiform = saref4water.AcceptabilityProperty("TotalColiform")
    TotalColiform.hasName.append("Total Coliform")
    TotalColiform.hasDescription.append(
        "Total Coliform in the sample")
    TotalColiformTest1.isMeasuredIn.append(MPN_per_100ML)
    TotalColiformTest1.relatesToProperty.append(TotalColiform)
    TotalColiformTest1.hasTimestamp.append(datetime.strptime("2022-03-06T21:01:30", '%Y-%m-%dT%H:%M:%S'))
    TotalColiformTest1.hasValue.append(240000)

    NickelTest1 = saref.Measurement("NickelTest1")
    NickelTest1.isMeasuredIn.append(mlperLitter)
    NickelTest1.relatesToProperty.append(saref4water.Nickel)
    NickelTest1.hasTimestamp.append(datetime.strptime("2022-03-06T21:01:30", '%Y-%m-%dT%H:%M:%S'))
    NickelTest1.hasValue.append(0.27)

    LeadTest1 = saref.Measurement("LeadTest1")
    LeadTest1.isMeasuredIn.append(mlperLitter)
    LeadTest1.relatesToProperty.append(saref4water.Lead)
    LeadTest1.hasTimestamp.append(datetime.strptime("2022-03-06T21:01:30", '%Y-%m-%dT%H:%M:%S'))
    LeadTest1.hasValue.append(0.31)

    ZincTest1 = saref.Measurement("ZincTest1")
    Zinc = saref4water.ChemicalProperty("Zinc")
    Zinc.hasName.append("Zinc")
    Zinc.hasDescription.append("Zinc")
    ZincTest1.isMeasuredIn.append(mlperLitter)
    ZincTest1.relatesToProperty.append(Zinc)
    ZincTest1.hasTimestamp.append(datetime.strptime("2022-03-06T21:01:30", '%Y-%m-%dT%H:%M:%S'))
    ZincTest1.hasValue.append(0.19)

    CooperTest1 = saref.Measurement("CooperTest1")
    CooperTest1.isMeasuredIn.append(mlperLitter)
    CooperTest1.relatesToProperty.append(saref4water.Copper)
    CooperTest1.hasTimestamp.append(datetime.strptime("2022-03-06T21:01:30", '%Y-%m-%dT%H:%M:%S'))
    CooperTest1.hasValue.append(0.31)

    CadmiumTest1 = saref.Measurement("CadmiumTest1")
    CadmiumTest1.isMeasuredIn.append(mlperLitter)
    CadmiumTest1.relatesToProperty.append(saref4water.Cadmium)
    CadmiumTest1.hasTimestamp.append(datetime.strptime("2022-03-06T21:01:30", '%Y-%m-%dT%H:%M:%S'))
    CadmiumTest1.hasValue.append(0.16)

    centralisedTreatment.hasMeasurement.append(phMeasurementTest1)
    centralisedTreatment.hasMeasurement.append(totalCODTest1)
    centralisedTreatment.hasMeasurement.append(filteredCODTest1)
    centralisedTreatment.hasMeasurement.append(BODTest1)
    centralisedTreatment.hasMeasurement.append(FilteredBODTest1)
    centralisedTreatment.hasMeasurement.append(TOCTEst1)
    centralisedTreatment.hasMeasurement.append(TurbidityTest1)
    centralisedTreatment.hasMeasurement.append(TKNTest1)
    centralisedTreatment.hasMeasurement.append(NH3Test1)
    centralisedTreatment.hasMeasurement.append(NH4Test1)
    centralisedTreatment.hasMeasurement.append(TotalNitrogenTest1)
    centralisedTreatment.hasMeasurement.append(TPTest1)
    centralisedTreatment.hasMeasurement.append(OPTest1)
    centralisedTreatment.hasMeasurement.append(TDSTest1)
    centralisedTreatment.hasMeasurement.append(AlkalinityTest1)
    centralisedTreatment.hasMeasurement.append(FatOilGreaseTest1)
    centralisedTreatment.hasMeasurement.append(ConductivityTest1)
    centralisedTreatment.hasMeasurement.append(SO4Test1)
    centralisedTreatment.hasMeasurement.append(SilicaSolubleTest1)
    centralisedTreatment.hasMeasurement.append(eColiTest1)
    centralisedTreatment.hasMeasurement.append(LegionaleaSSPTest1)
    centralisedTreatment.hasMeasurement.append(CampylobacterSPPTest1)
    centralisedTreatment.hasMeasurement.append(SalmonellaSPPTest1)
    centralisedTreatment.hasMeasurement.append(PseudomonasSPPTest1)
    centralisedTreatment.hasMeasurement.append(StaphylococcusAureusTest1)
    centralisedTreatment.hasMeasurement.append(TotalCountTest1)
    centralisedTreatment.hasMeasurement.append(TotalColiformTest1)
    centralisedTreatment.hasMeasurement.append(NickelTest1)
    centralisedTreatment.hasMeasurement.append(LeadTest1)
    centralisedTreatment.hasMeasurement.append(ZincTest1)
    centralisedTreatment.hasMeasurement.append(CooperTest1)
    centralisedTreatment.hasMeasurement.append(CadmiumTest1)


    pilotPlantTreatment = wsisSchema.ResourceProducer("PilotPlantTreatment")
    pilotPlantTreatment.hasName.append("Pilot Treatment Plant")
    DAF.usesTechnology.append(pilotPlantTreatment)

    holdingTank = wsisSchema.Technology("HoldingTank")
    holdingTank.hasName.append("Holding Tank")
    pilotPlantTreatment.usesTechnology.append(holdingTank)
    holdingTank.canProcess.append(waterDAF)
    waterHoldingTank = saref4water.Water("waterHoldingTank")
    holdingTank.generates.append(waterHoldingTank)

    membraneBioReactor = wsisSchema.Technology("MembraneBioReactor")
    membraneBioReactor.hasName.append("Membrane Bioreactor")
    holdingTank.usesTechnology.append(membraneBioReactor)
    membraneBioReactor.canProcess.append(waterHoldingTank)

    waterMembraneBioReactor = saref4water.Water("waterMembraneBioReactor")
    membraneBioReactor.generates.append(waterMembraneBioReactor)

    WAS= wsisSchema.SolidMaterial ("WAS")
    membraneBioReactor.generates.append(WAS)
    RAS = wsisSchema.SolidMaterial("RAS")
    membraneBioReactor.generates.append(RAS)

    membraneBioReactor.canProcess.append(RAS)

    ionExchange = wsisSchema.Technology("IonExchange")
    ionExchange.hasName.append("Ion Exchange")
    membraneBioReactor.usesTechnology.append(ionExchange)
    ionExchange.canProcess.append(waterMembraneBioReactor)

    waterIonExchange = saref4water.Water("waterIonExchange")
    ionExchange.generates.append(waterIonExchange)
    wasteIonExchange = wsisSchema.SolidMaterial("WasteIonExchange")
    ionExchange.generates.append(wasteIonExchange)

    UVH2O2 = wsisSchema.Technology("UVH2O2")
    UVH2O2.hasName.append("UVH2O2")
    ionExchange.usesTechnology.append(UVH2O2)
    UVH2O2.canProcess.append(waterIonExchange)

    treatedWater = saref4water.Water ("TreatedWater")
    UVH2O2.generates.append(treatedWater)

    agricola.canProcess.append(treatedWater)


    return wsisSchema

def CS6_TUPRAS(wsisSchema):
    saref4water = get_namespace("https://saref.etsi.org/saref4watr/")
    saref = get_namespace("https://saref.etsi.org/core/")
    om = get_namespace("http://www.ontology-of-units-of-measure.org/resource/om-2/")
    izmit = wsisSchema.Industry("Izmit")
    izmit.hasName.append("Izmit Refinery")
    izmit.hasDescription.append(
        "İzmit Refinery began production in 1961 with capacity to process 1 million tons/year crude oil. As a result of significant capacity increases and the conversion unit investments over the years, the Refinery's design capacity was registered at 11.3 million tons/year. Producing to Euro V standards, İzmit Refinery located in a consumption center, accounting for 33/100 of Turkey's consuption of petroleum products.")
    izmit.hasOwner.append("Tüpraş")

    WaterTK961 = saref4water.Water("WaterTK961")
    WaterTK961.hasName.append("TK961 Tank Water")
    WaterTK967 = saref4water.Water("WaterTK967")
    WaterTK967.hasName.append("TK967 Tank Water")
    inputStreamMixingValve = wsisSchema.Technology("MixingValve")
    inputStreamMixingValve.hasName.append("Mixing Valve")
    inputStreamMixingValve.canProcess.append(WaterTK961)
    inputStreamMixingValve.canProcess.append(WaterTK967)

    ph = saref4water.AcceptabilityProperty("ph")
    ph.hasName.append("pH")
    ph.hasDescription.append("Quantitative measure of the acidity or basicity of aqueous or other liquid solutions")

    pHWaterTK961 = saref.Measurement("pHWaterTK961")
    pHWaterTK961.relatesToProperty.append(ph)
    WaterTK961.hasMeasurement.append(pHWaterTK961)

    pHWaterTK967 = saref.Measurement("pHWaterTK967")
    pHWaterTK967.relatesToProperty.append(ph)
    WaterTK967.hasMeasurement.append(pHWaterTK967)

    ppm = saref.UnitOfMeasure("ppm")
    ppm.hasName.append("parts-per-million")
    ppm.hasDescription.append(
        "Parts-per notation is often used describing dilute solutions in chemistry, for instance, the relative abundance of dissolved minerals or pollutants in water. The quantity '1 ppm' can be used for a mass fraction if a water-borne pollutant is present at one-millionth of a gram per gram of sample solution")

    totalCOD = saref4water.AcceptabilityProperty("totalCOD")
    totalCOD.hasName.append("total COD")
    totalCOD.hasDescription.append(
        "The COD is the estimate of oxygen required for the portion of organic matter in wastewater that is subjected to oxidation and also the amount of oxygen consumed by organic matter from boiling acid potassium dichromate solution.")

    totalCODTK961 = saref.Measurement("totalCODTK961")
    totalCODTK961.relatesToProperty.append(totalCOD)
    totalCODTK961.isMeasuredIn.append(ppm)
    WaterTK961.hasMeasurement.append(totalCODTK961)

    totalCODWaterTK967 = saref.Measurement("totalCODWaterTK967")
    totalCODWaterTK967.relatesToProperty.append(totalCOD)
    totalCODWaterTK967.isMeasuredIn.append(ppm)
    WaterTK967.hasMeasurement.append(totalCODWaterTK967)

    AmmoniumCation = saref4water.ChemicalProperty("N-NH4")
    AmmoniumCation.hasName.append("Ammonium Cation")
    AmmoniumCation.hasDescription.append(
        "The ammonium cation is a positively-charged polyatomic ion with the chemical formula NH+4 or [NH 4] +")

    TKNWaterTK961 = saref.Measurement("TKNWaterTK961")
    TKNWaterTK961.relatesToProperty.append(AmmoniumCation)
    TKNWaterTK961.isMeasuredIn.append(ppm)
    WaterTK961.hasMeasurement.append(TKNWaterTK961)

    TKNWaterTK967 = saref.Measurement("TKNWaterTK967")
    TKNWaterTK967.relatesToProperty.append(AmmoniumCation)
    TKNWaterTK967.isMeasuredIn.append(ppm)
    WaterTK967.hasMeasurement.append(TKNWaterTK967)

    Sulfide = saref4water.ChemicalProperty("Sulfide")
    Sulfide.hasName.append("Sulfide")
    Sulfide.hasDescription.append("an inorganic anion of sulfur")

    SulfideWaterTK961 = saref.Measurement("SulfideWaterTK961")
    SulfideWaterTK961.relatesToProperty.append(Sulfide)
    SulfideWaterTK961.isMeasuredIn.append(ppm)
    WaterTK961.hasMeasurement.append(SulfideWaterTK961)

    SulfideWaterTK967 = saref.Measurement("SulfideWaterTK967")
    SulfideWaterTK967.relatesToProperty.append(Sulfide)
    SulfideWaterTK967.isMeasuredIn.append(ppm)
    WaterTK967.hasMeasurement.append(SulfideWaterTK967)

    microSiemmensPerCm = saref.UnitOfMeasure("microSiemmensPerCm")
    microSiemmensPerCm.hasName.append("\u03BCS/cm")

    ConductivityWaterTK961 = saref.Measurement("ConductivityWaterTK961")
    ConductivityWaterTK961.relatesToProperty.append(saref4water.Conductivity)
    ConductivityWaterTK961.isMeasuredIn.append(microSiemmensPerCm)
    WaterTK961.hasMeasurement.append(ConductivityWaterTK961)

    ConductivityWaterTK967 = saref.Measurement("ConductivityWaterTK967")
    ConductivityWaterTK967.relatesToProperty.append(saref4water.Conductivity)
    ConductivityWaterTK967.isMeasuredIn.append(microSiemmensPerCm)
    WaterTK967.hasMeasurement.append(ConductivityWaterTK967)

    cubicMetrePerHour = saref.UnitOfMeasure("cubicMetrePerHour")
    cubicMetrePerHour.hasName.append("m^3/h")

    FlowRateWaterTK961 = saref.Measurement("FlowRateWaterTK961")
    FlowRateWaterTK961.relatesToProperty.append(saref4water.FlowRate)
    FlowRateWaterTK961.isMeasuredIn.append(cubicMetrePerHour)
    WaterTK961.hasMeasurement.append(FlowRateWaterTK961)

    FlowRateWaterTK967 = saref.Measurement("FlowRateWaterTK967")
    FlowRateWaterTK967.relatesToProperty.append(saref4water.FlowRate)
    FlowRateWaterTK967.isMeasuredIn.append(cubicMetrePerHour)
    WaterTK967.hasMeasurement.append(FlowRateWaterTK967)

    FTU = saref.UnitOfMeasure("FTU")
    FTU.hasName.append("Formazine Turbidity Unit")
    FTU.hasDescription.append(
        "FTU became the defined unit of measurement after the acceptance of Formazine as the primary reference standard for turbidity. FTU, as well as any measurement unit derived from, or that references FTU does not specify how a device measures turbidity in a water sample")
    TurbidityMixingValve = saref.Measurement("TurbidityMixingValve")
    TurbidityMixingValve.isMeasuredIn.append(FTU)
    TurbidityMixingValve.relatesToProperty.append(saref4water.Turbidity)
    inputStreamMixingValve.hasMeasurement.append(TurbidityMixingValve)

    WaterInputBallastTreatmentPlant = saref4water.Water("WaterInputBallastTreatmentPlant")
    inputStreamMixingValve.generates.append(WaterInputBallastTreatmentPlant)

    ballastTreatmentPlant = wsisSchema.Process("BallastTreatmentPlant")
    TPS = wsisSchema.Technology("TPS")
    TPS.hasName.append("Tilted plate separator")
    TPS.canProcess.append(WaterInputBallastTreatmentPlant)
    WaterOutputTPS = saref4water.Water("WaterOutputTPS")
    TPS.generates.append(WaterOutputTPS)
    ballastTreatmentPlant.usesTechnology.append(TPS)

    FMB = wsisSchema.Technology("FMB")
    FMB.hasName.append("Flesh Mixin Basin")
    FMB.canProcess.append(WaterOutputTPS)
    WaterOutputFMB = saref4water.Water("WaterOutputFMB")
    FMB.generates.append(WaterOutputFMB)
    ballastTreatmentPlant.usesTechnology.append(FMB)

    CFB = wsisSchema.Technology("CFB")
    CFB.hasName.append("Coagulation-Floculation Basin")
    CFB.canProcess.append(WaterOutputFMB)
    WaterOutputCFB = saref4water.Water("WaterOutputCFB")
    CFB.generates.append(WaterOutputCFB)
    ballastTreatmentPlant.usesTechnology.append(CFB)

    DAFB = wsisSchema.Technology("DAFB")
    DAFB.hasName.append("Dissolved Air Flotation Basin")
    DAFB.canProcess.append(WaterOutputCFB)
    WaterOutputDAFB = saref4water.Water("WaterOutputDAFB")
    DAFB.generates.append(WaterOutputDAFB)
    ballastTreatmentPlant.usesTechnology.append(DAFB)

    FlowRateAirInletDAFB = saref.Measurement("FlowRateAirInletDAFB")
    FlowRateAirInletDAFB.relatesToProperty.append(saref4water.FlowRate)
    FlowRateAirInletDAFB.isMeasuredIn.append(cubicMetrePerHour)
    DAFB.hasMeasurement.append(FlowRateAirInletDAFB)

    TurbidityDAFB = saref.Measurement("TurbidityDAFB")
    TurbidityDAFB.isMeasuredIn.append(FTU)
    TurbidityDAFB.relatesToProperty.append(saref4water.Turbidity)
    DAFB.hasMeasurement.append(TurbidityDAFB)

    CB = wsisSchema.Technology("CB")
    CB.hasName.append("Check Basin")
    CB.canProcess.append(WaterOutputCFB)
    WaterOutputCB = saref4water.Water("WaterOutputCB")
    CB.generates.append(WaterOutputCB)
    ballastTreatmentPlant.usesTechnology.append(CB)

    pHWaterOutputCB = saref.Measurement("pHWaterOutputCB")
    pHWaterOutputCB.relatesToProperty.append(ph)
    WaterOutputCB.hasMeasurement.append(pHWaterOutputCB)

    totalCODWaterOutputCB = saref.Measurement("totalCODWaterOutputCB")
    totalCODWaterOutputCB.relatesToProperty.append(totalCOD)
    totalCODWaterOutputCB.isMeasuredIn.append(ppm)
    WaterOutputCB.hasMeasurement.append(totalCODWaterOutputCB)

    TKNWaterOutputCB = saref.Measurement("TKNWaterOutputCB")
    TKNWaterOutputCB.relatesToProperty.append(AmmoniumCation)
    TKNWaterOutputCB.isMeasuredIn.append(ppm)
    WaterOutputCB.hasMeasurement.append(TKNWaterOutputCB)

    SulfideWaterOutputCB = saref.Measurement("SulfideWaterOutputCB")
    SulfideWaterOutputCB.relatesToProperty.append(Sulfide)
    SulfideWaterOutputCB.isMeasuredIn.append(ppm)
    WaterOutputCB.hasMeasurement.append(SulfideWaterOutputCB)

    ConductivityWaterOutputCB = saref.Measurement("ConductivityWaterOutputCB")
    ConductivityWaterOutputCB.relatesToProperty.append(saref4water.Conductivity)
    ConductivityWaterOutputCB.isMeasuredIn.append(microSiemmensPerCm)
    WaterOutputCB.hasMeasurement.append(ConductivityWaterOutputCB)

    TurbidityWaterOutputCB = saref.Measurement("TurbidityWaterOutputCB")
    TurbidityWaterOutputCB.isMeasuredIn.append(FTU)
    TurbidityWaterOutputCB.relatesToProperty.append(saref4water.Turbidity)
    WaterOutputCB.hasMeasurement.append(TurbidityWaterOutputCB)

    BT = wsisSchema.Technology("BT")
    BT.hasName.append("Biological Treatment")
    BT.canProcess.append(WaterOutputCB)
    WaterOutputBT = saref4water.Water("WaterOutputBT")
    BT.generates.append(WaterOutputBT)
    ballastTreatmentPlant.usesTechnology.append(BT)

    BT = wsisSchema.Technology("BT")
    BT.hasName.append("Biological Treatment")
    BT.canProcess.append(WaterOutputCB)
    WaterOutputBT = saref4water.Water("WaterOutputBT")
    BT.generates.append(WaterOutputBT)
    ballastTreatmentPlant.usesTechnology.append(BT)

    FC = wsisSchema.Technology("FC")
    FC.hasName.append("Final Clarifier")
    FC.canProcess.append(WaterOutputCB)
    WaterOutputFC = saref4water.Water("WaterOutputFC")
    FC.generates.append(WaterOutputFC)
    ballastTreatmentPlant.usesTechnology.append(FC)

    ballastTreatmentPlant.generates.append(WaterOutputCB)
    ballastTreatmentPlant.generates.append(WaterOutputFC)

    return wsisSchema

def agricola_instances(wsisSchema):
    saref4water = get_namespace("https://saref.etsi.org/saref4watr/")
    saref = get_namespace("https://saref.etsi.org/core/")
    om = get_namespace("http://www.ontology-of-units-of-measure.org/resource/om-2/")

    agricola = wsisSchema.Industry("AgricolaCaseStudy")
    agricola.hasDescription.append(
        "Agricola SA is a well-known top private meat group of companies located in Bacău County, Romania, which delivers, on a daily basis, approximate 100,000 chickens (more than 150 tonnes of meat). The Group Agricola SA consists of more companies: Agricola Internațional (Fodder production, 4 specialized farms in poultry breeding, 15 chicken farms and a slaughterhouse); Salbac (Cured salamis and boiled/smoked meat products); Europrod (Ready-meals and ready-to-eat products); Avicola Lumina, Constanța county (18 modernized warehouses of laying hens); Aicbac (cereal production for fodders, a small dairy farm and dairy processing unit). Besides, there is also a factory for egg powder production.")
    agricola.hasOwner.append("Agricola Internațional SA")
    agricola.hasName.append("Agricola Demo Site")

    pre_screening1 = wsisSchema.Technology("PreScreening")
    pre_screening1.hasDescription.append(
        "Screening is often used to remove large pieces of waste so that the water can be reused within the processing plant")
    pre_screening1.hasName.append("Pre-screening")
    agricola.usesTechnology.append(pre_screening1)

    water_operation = saref4water.Water("WaterOperation")
    pre_screening1.canProcess.append(water_operation)

    sludgePreScreening = wsisSchema.SemiSolidMaterial("PreScreeningSludge")
    waterPreScreening = saref4water.Water("WaterPreScreening")
    pre_screening1.generates.append(sludgePreScreening)
    pre_screening1.generates.append(waterPreScreening)

    mixing_tank = wsisSchema.Technology("MixingTank")
    mixing_tank.hasName.append("Mixing Tank")
    pre_screening1.usesTechnology.append(mixing_tank)
    coagulant = wsisSchema.SolidMaterial("FeCl3")
    flocculant = wsisSchema.SolidMaterial("NaOH")
    mixing_tank.canProcess.append(coagulant)
    mixing_tank.canProcess.append(flocculant)
    mixing_tank.canProcess.append(waterPreScreening)
    waterMixingTank = saref4water.Water("waterGeneratedByMixingTank")
    mixing_tank.generates.append(waterMixingTank)

    DAF = wsisSchema.Technology("DAF")
    DAF.hasName.append("DAF")
    mixing_tank.usesTechnology.append(DAF)
    DAF.canProcess.append(waterMixingTank)
    Air_daf = wsisSchema.Air("AirInDaf")
    DAF.canProcess.append(Air_daf)
    sludgeDAF = wsisSchema.SemiSolidMaterial("sludgeDAF")
    DAF.generates.append(sludgeDAF)
    waterDAF = saref4water.Water("waterDAF")
    DAF.generates.append(waterDAF)

    centralisedTreatment = wsisSchema.Technology("CentralisedTreatment")
    centralisedTreatment.hasName.append("Centralised Treatment Plant")
    DAF.usesTechnology.append(centralisedTreatment)
    centralisedTreatment.canProcess.append(sludgeDAF)
    centralisedTreatment.canProcess.append(waterDAF)

    phMeasurementTest1 = saref.Measurement("phMeasurementTest1")
    ph = saref4water.AcceptabilityProperty("ph")
    ph.hasName.append("pH")
    ph.hasDescription.append("Quantitative measure of the acidity or basicity of aqueous or other liquid solutions")
    phMeasurementTest1.relatesToProperty.append(ph)
    phMeasurementTest1.hasTimestamp.append(datetime.strptime("2022-03-06T21:01:30", '%Y-%m-%dT%H:%M:%S'))
    phMeasurementTest1.hasValue.append(8.48)

    totalCODTest1 = saref.Measurement("TotalCODTest1")
    totalCOD = saref4water.AcceptabilityProperty("totalCOD")
    totalCOD.hasName.append("total COD")
    totalCOD.hasDescription.append(
        "The COD is the estimate of oxygen required for the portion of organic matter in wastewater that is subjected to oxidation and also the amount of oxygen consumed by organic matter from boiling acid potassium dichromate solution.")

    totalCODTest1.relatesToProperty.append(totalCOD)
    totalCODTest1.hasTimestamp.append(datetime.strptime("2022-03-06T21:01:30", '%Y-%m-%dT%H:%M:%S'))
    totalCODTest1.hasValue.append(126)
    mlperLitter = om.PrefixedGramPerLitre("milligramPerLitre")
    totalCODTest1.isMeasuredIn.append(mlperLitter)

    filteredCODTest1 = saref.Measurement("FilteredCODTest1")
    filteredCOD = saref4water.AcceptabilityProperty("filteredCOD")
    filteredCOD.hasName.append("filtered COD")
    filteredCODTest1.isMeasuredIn.append(mlperLitter)
    filteredCODTest1.relatesToProperty.append(filteredCOD)
    filteredCODTest1.hasTimestamp.append(datetime.strptime("2022-03-06T21:01:30", '%Y-%m-%dT%H:%M:%S'))
    filteredCODTest1.hasValue.append(101)

    BODTest1 = saref.Measurement("BODTEst1")
    BOD = saref4water.AcceptabilityProperty("BOD")
    BOD.hasName.append("BOD")
    BOD.hasDescription.append(
        "BOD is defined as the amount of dissolved oxygen needed by aerobic biological organisms in a body of water to break down the organic material present in a water sample, at a specific temperature and specified period")
    BODTest1.isMeasuredIn.append(mlperLitter)
    BODTest1.relatesToProperty.append(BOD)
    BODTest1.hasTimestamp.append(datetime.strptime("2022-03-06T21:01:30", '%Y-%m-%dT%H:%M:%S'))
    BODTest1.hasValue.append(44)

    FilteredBODTest1 = saref.Measurement("FilteredBODTEst1")
    FilteredBOD = saref4water.AcceptabilityProperty("FilteredBOD")
    FilteredBOD.hasName.append("Filtered BOD")
    FilteredBODTest1.isMeasuredIn.append(mlperLitter)
    FilteredBODTest1.relatesToProperty.append(FilteredBOD)
    FilteredBODTest1.hasTimestamp.append(datetime.strptime("2022-03-06T21:01:30", '%Y-%m-%dT%H:%M:%S'))
    FilteredBODTest1.hasValue.append(39)

    TOCTEst1 = saref.Measurement("TOCTest1")
    TOC = saref4water.AcceptabilityProperty("TotalOrganicCarbon")
    TOC.hasName.append("Total Organic Carbon")
    TOCTEst1.isMeasuredIn.append(mlperLitter)
    TOCTEst1.relatesToProperty.append(TOC)
    TOCTEst1.hasTimestamp.append(datetime.strptime("2022-03-06T21:01:30", '%Y-%m-%dT%H:%M:%S'))
    TOCTEst1.hasValue.append(20.5)

    TSSTest1 = saref.Measurement("TSSTest1")
    TSSTest1.isMeasuredIn.append(mlperLitter)
    TSSTest1.relatesToProperty.append(saref4water.TotalSuspendedSolids)
    TSSTest1.hasTimestamp.append(datetime.strptime("2022-03-06T21:01:30", '%Y-%m-%dT%H:%M:%S'))
    TSSTest1.hasValue.append(7)

    ISSTest1 = saref.Measurement("ISSTEst1")
    ISS = saref4water.AcceptabilityProperty("ISS")
    ISS.hasName.append("ISS")
    ISS.hasDescription.append("ISS")
    ISSTest1.isMeasuredIn.append(mlperLitter)
    ISSTest1.relatesToProperty.append(ISS)
    ISSTest1.hasTimestamp.append(datetime.strptime("2022-03-06T21:01:30", '%Y-%m-%dT%H:%M:%S'))
    ISSTest1.hasValue.append(1024)

    TurbidityTest1 = saref.Measurement("TurbidityTEst1")
    FTU = saref.UnitOfMeasure("FTU")
    FTU.hasName.append("Formazine Turbidity Unit")
    FTU.hasDescription.append(
        "FTU became the defined unit of measurement after the acceptance of Formazine as the primary reference standard for turbidity. FTU, as well as any measurement unit derived from, or that references FTU does not specify how a device measures turbidity in a water sample")
    TurbidityTest1.isMeasuredIn.append(FTU)
    TurbidityTest1.relatesToProperty.append(saref4water.Turbidity)
    TurbidityTest1.hasTimestamp.append(datetime.strptime("2022-03-06T21:01:30", '%Y-%m-%dT%H:%M:%S'))
    TurbidityTest1.hasValue.append(30)

    TKNTest1 = saref.Measurement("TKNTEst1")
    TKN = saref4water.AcceptabilityProperty("TKN")
    TKN.hasName.append("Total Kjeldahl Nitrogen")
    TKN.hasDescription.append(
        "Total Kjeldahl Nitrogen means the sum of free-ammonia and organic nitrogen compounds, which are converted to ammonium sulfate (NH4)2SO4, under test conditions.")
    TKNTest1.isMeasuredIn.append(mlperLitter)
    TKNTest1.relatesToProperty.append(TKN)
    TKNTest1.hasTimestamp.append(datetime.strptime("2022-03-06T21:01:30", '%Y-%m-%dT%H:%M:%S'))
    TKNTest1.hasValue.append(48.73)

    NH3Test1 = saref.Measurement("NH3Test1")
    Ammonia = saref4water.ChemicalProperty("TKN")
    Ammonia.hasName.append("Ammonia")
    Ammonia.hasDescription.append(
        "Ammonia is an inorganic compound of nitrogen and hydrogen with the formula NH 3.")
    NH3Test1.isMeasuredIn.append(mlperLitter)
    NH3Test1.relatesToProperty.append(Ammonia)
    NH3Test1.hasTimestamp.append(datetime.strptime("2022-03-06T21:01:30", '%Y-%m-%dT%H:%M:%S'))
    NH3Test1.hasValue.append(8.81)

    NH4Test1 = saref.Measurement("NH4Test1")
    AmmoniumCation = saref4water.ChemicalProperty("TKN")
    AmmoniumCation.hasName.append("Ammonium Cation")
    AmmoniumCation.hasDescription.append(
        "The ammonium cation is a positively-charged polyatomic ion with the chemical formula NH+4 or [NH 4] +")
    NH4Test1.isMeasuredIn.append(mlperLitter)
    NH4Test1.relatesToProperty.append(AmmoniumCation)
    NH4Test1.hasTimestamp.append(datetime.strptime("2022-03-06T21:01:30", '%Y-%m-%dT%H:%M:%S'))
    NH4Test1.hasValue.append(9.32)

    NO3Test1 = saref.Measurement("NO3Test1")
    NO3Test1.isMeasuredIn.append(mlperLitter)
    NO3Test1.relatesToProperty.append(saref4water.Nitrate)
    NO3Test1.hasTimestamp.append(datetime.strptime("2022-03-06T21:01:30", '%Y-%m-%dT%H:%M:%S'))
    NO3Test1.hasValue.append(11.8)

    TotalNitrogenTest1 = saref.Measurement("TotalNitrogenTest1")
    TotalNitrogen = saref4water.ChemicalProperty("TN")
    TotalNitrogen.hasName.append("Total Nitrogen")
    TotalNitrogen.hasDescription.append(
        "Total Nitrogen is the sum of nitrate (NO3), nitrite (NO2), organic nitrogen and ammonia (all expressed as N). Note that for laboratory analysis purposes, Total")
    TotalNitrogenTest1.isMeasuredIn.append(mlperLitter)
    TotalNitrogenTest1.relatesToProperty.append(TotalNitrogen)
    TotalNitrogenTest1.hasTimestamp.append(datetime.strptime("2022-03-06T21:01:30", '%Y-%m-%dT%H:%M:%S'))
    TotalNitrogenTest1.hasValue.append(30.4)

    TPTest1 = saref.Measurement("TPTest1")
    TP = saref4water.AcceptabilityProperty("TP")
    TP.hasName.append("TP")
    TP.hasDescription.append("TP")
    TPTest1.isMeasuredIn.append(mlperLitter)
    TPTest1.relatesToProperty.append(TP)
    TPTest1.hasTimestamp.append(datetime.strptime("2022-03-06T21:01:30", '%Y-%m-%dT%H:%M:%S'))
    TPTest1.hasValue.append(1190)

    OPTest1 = saref.Measurement("OPTest1")
    OP = saref4water.ChemicalProperty("Ortho Phosphate")
    OP.hasName.append("OP")
    OP.hasDescription.append(
        "The phosphate or orthophosphate ion [PO4]3−is derived from phosphoric acid by the removal of three protons H+. Removal of one or two protons gives the dihydrogen phosphate ion [H 2PO4]− and the hydrogen phosphate ion [HPO4]2−ion, respectively. These names are also used for salts of those anions, such as ammonium dihydrogen phosphate and trisodium phosphate.")
    OPTest1.isMeasuredIn.append(mlperLitter)
    OPTest1.relatesToProperty.append(OP)
    OPTest1.hasTimestamp.append(datetime.strptime("2022-03-06T21:01:30", '%Y-%m-%dT%H:%M:%S'))
    OPTest1.hasValue.append(3.45)

    TDSTest1 = saref.Measurement("TDSTest1")
    TDSTest1.isMeasuredIn.append(mlperLitter)
    TDSTest1.relatesToProperty.append(saref4water.TotalDissolvedSolids)
    TDSTest1.hasTimestamp.append(datetime.strptime("2022-03-06T21:01:30", '%Y-%m-%dT%H:%M:%S'))
    TDSTest1.hasValue.append(1190)

    AlkalinityTest1 = saref.Measurement("AlkalinityTest1")
    Alkalinity = saref4water.AcceptabilityProperty("Alkalinity")
    Alkalinity.hasName.append("Alkalinity")
    Alkalinity.hasDescription.append(
        "Total alkalinity is measured by collecting a water sample, and measuring the amount of acid needed to bring the sample to a pH of 4.2.")
    AlkalinityTest1.isMeasuredIn.append(mlperLitter)
    AlkalinityTest1.relatesToProperty.append(Alkalinity)
    AlkalinityTest1.hasTimestamp.append(datetime.strptime("2022-03-06T21:01:30", '%Y-%m-%dT%H:%M:%S'))
    AlkalinityTest1.hasValue.append(45)

    FatOilGreaseTest1 = saref.Measurement("FatOilGreaseTest1")
    FatOilGrease = saref4water.AcceptabilityProperty("FatOilGrease")
    FatOilGrease.hasName.append("Fat, Oil, Grease")
    FatOilGrease.hasDescription.append(
        "NMR is a bulk measurement technique which selectively measures all of the oil and fat in the sample regardless of the distribution of the grease")
    FatOilGreaseTest1.isMeasuredIn.append(mlperLitter)
    FatOilGreaseTest1.relatesToProperty.append(FatOilGrease)
    FatOilGreaseTest1.hasTimestamp.append(datetime.strptime("2022-03-06T21:01:30", '%Y-%m-%dT%H:%M:%S'))
    FatOilGreaseTest1.hasValue.append(5.5)

    ConductivityTest1 = saref.Measurement("ConductivityTest1")
    microSiemmensPerCm = saref.UnitOfMeasure("microSiemmensPerCm")
    microSiemmensPerCm.hasName.append("\u03BCS/cm")
    ConductivityTest1.isMeasuredIn.append(mlperLitter)
    ConductivityTest1.relatesToProperty.append(saref4water.Conductivity)
    ConductivityTest1.hasTimestamp.append(datetime.strptime("2022-03-06T21:01:30", '%Y-%m-%dT%H:%M:%S'))
    ConductivityTest1.hasValue.append(1263)

    SO4Test1 = saref.Measurement("So4Test1")
    SO4Test1.isMeasuredIn.append(mlperLitter)
    SO4Test1.relatesToProperty.append(saref4water.Sulphate)
    SO4Test1.hasTimestamp.append(datetime.strptime("2022-03-06T21:01:30", '%Y-%m-%dT%H:%M:%S'))
    SO4Test1.hasValue.append(90.2)

    SilicaSolubleTest1 = saref.Measurement("SilicaSlubleTest1")
    SilicaSoluble = saref4water.ChemicalProperty("SilicaSoluble")
    SilicaSoluble.hasName.append("Silica Soluble")
    SilicaSoluble.hasDescription.append(
        "The silica dissolved and crystallized in the presence of surface seed crystals, ultimately forming a hollow-structured zeolite during crystallization.")
    SilicaSolubleTest1.isMeasuredIn.append(mlperLitter)
    SilicaSolubleTest1.relatesToProperty.append(saref4water.Sulphate)
    SilicaSolubleTest1.hasTimestamp.append(datetime.strptime("2022-03-06T21:01:30", '%Y-%m-%dT%H:%M:%S'))
    SilicaSolubleTest1.hasValue.append('7.80/3.68')

    eColiTest1 = saref.Measurement("eColiTest1")
    MPN_per_100ML = saref.UnitOfMeasure("microSiemmensPerCm")
    MPN_per_100ML.hasName.append("MPN/100ml")
    eColiTest1.isMeasuredIn.append(MPN_per_100ML)
    eColiTest1.relatesToProperty.append(saref4water.EscherichiaColi)
    eColiTest1.hasTimestamp.append(datetime.strptime("2022-03-06T21:01:30", '%Y-%m-%dT%H:%M:%S'))
    eColiTest1.hasValue.append(4800)

    LegionaleaSSPTest1 = saref.Measurement("LegionaleaSSPTest1")
    Legionella = saref4water.BacterialProperty("Legionella")
    Legionella.hasName.append("Legionella")
    Legionella.hasDescription.append(
        "Legionella is a genus of pathogenic gram-negative bacteria that includes the species L. pneumophila, ")
    LegionaleaSSPTest1.isMeasuredIn.append(MPN_per_100ML)
    LegionaleaSSPTest1.relatesToProperty.append(Legionella)
    LegionaleaSSPTest1.hasTimestamp.append(datetime.strptime("2022-03-06T21:01:30", '%Y-%m-%dT%H:%M:%S'))
    LegionaleaSSPTest1.hasValue.append(0)

    CampylobacterSPPTest1 = saref.Measurement("CampylobacterSPPTest1")
    Campylobacter = saref4water.BacterialProperty("Campylobacter")
    Campylobacter.hasName.append("Campylobacter")
    Campylobacter.hasDescription.append(
        "Campylobacter (meaning 'curved bacteria') is a genus of Gram-negative bacteria.")
    CampylobacterSPPTest1.isMeasuredIn.append(MPN_per_100ML)
    CampylobacterSPPTest1.relatesToProperty.append(Legionella)
    CampylobacterSPPTest1.hasTimestamp.append(datetime.strptime("2022-03-06T21:01:30", '%Y-%m-%dT%H:%M:%S'))
    CampylobacterSPPTest1.hasValue.append(0)

    SalmonellaSPPTest1 = saref.Measurement("SalmonellaSPPTest1")
    Salmonella = saref4water.BacterialProperty("Salmonella")
    Salmonella.hasName.append("Salmonella")
    Salmonella.hasDescription.append(
        "Salmonella infection (salmonellosis) is a common bacterial disease that affects the intestinal tract. ")
    SalmonellaSPPTest1.isMeasuredIn.append(MPN_per_100ML)
    SalmonellaSPPTest1.relatesToProperty.append(Legionella)
    SalmonellaSPPTest1.hasTimestamp.append(datetime.strptime("2022-03-06T21:01:30", '%Y-%m-%dT%H:%M:%S'))
    SalmonellaSPPTest1.hasValue.append('Presence')

    PseudomonasSPPTest1 = saref.Measurement("SalmonellaSPPTest1")
    Pseudomonas = saref4water.BacterialProperty("Pseudomonas")
    Pseudomonas.hasName.append("Pseudomonas")
    Pseudomonas.hasDescription.append(
        "Pseudomonas is a genus of Gram-negative, Gammaproteobacteria, belonging to the family Pseudomonadaceae and containing 191 described species ")
    PseudomonasSPPTest1.isMeasuredIn.append(MPN_per_100ML)
    PseudomonasSPPTest1.relatesToProperty.append(Pseudomonas)
    PseudomonasSPPTest1.hasTimestamp.append(datetime.strptime("2022-03-06T21:01:30", '%Y-%m-%dT%H:%M:%S'))
    PseudomonasSPPTest1.hasValue.append(900)

    StaphylococcusAureusTest1 = saref.Measurement("SalmonellaSPPTest1")
    StaphylococcusAureus = saref4water.BacterialProperty("StaphylococcusAureus")
    StaphylococcusAureus.hasName.append("StaphylococcusAureus")
    StaphylococcusAureus.hasDescription.append(
        "Staphylococcus aureus or “staph” is a type of bacteria found on human skin, in the nose, armpit, groin, and other areas. ")
    StaphylococcusAureusTest1.isMeasuredIn.append(MPN_per_100ML)
    StaphylococcusAureusTest1.relatesToProperty.append(StaphylococcusAureus)
    StaphylococcusAureusTest1.hasTimestamp.append(datetime.strptime("2022-03-06T21:01:30", '%Y-%m-%dT%H:%M:%S'))
    StaphylococcusAureusTest1.hasValue.append(280)

    TotalCountTest1 = saref.Measurement("TotalCountTest1")
    TotalCount = saref4water.AcceptabilityProperty("TotalCount")
    TotalCount.hasName.append("Total Count")
    TotalCount.hasDescription.append(
        "Total Count og micro-organims")
    TotalCountTest1.isMeasuredIn.append(MPN_per_100ML)
    TotalCountTest1.relatesToProperty.append(TotalCount)
    TotalCountTest1.hasTimestamp.append(datetime.strptime("2022-03-06T21:01:30", '%Y-%m-%dT%H:%M:%S'))
    TotalCountTest1.hasValue.append(2020000)

    TotalColiformTest1 = saref.Measurement("TotalColiformTest1")
    TotalColiform = saref4water.AcceptabilityProperty("TotalColiform")
    TotalColiform.hasName.append("Total Coliform")
    TotalColiform.hasDescription.append(
        "Total Coliform in the sample")
    TotalColiformTest1.isMeasuredIn.append(MPN_per_100ML)
    TotalColiformTest1.relatesToProperty.append(TotalColiform)
    TotalColiformTest1.hasTimestamp.append(datetime.strptime("2022-03-06T21:01:30", '%Y-%m-%dT%H:%M:%S'))
    TotalColiformTest1.hasValue.append(240000)

    NickelTest1 = saref.Measurement("NickelTest1")
    NickelTest1.isMeasuredIn.append(mlperLitter)
    NickelTest1.relatesToProperty.append(saref4water.Nickel)
    NickelTest1.hasTimestamp.append(datetime.strptime("2022-03-06T21:01:30", '%Y-%m-%dT%H:%M:%S'))
    NickelTest1.hasValue.append(0.27)

    LeadTest1 = saref.Measurement("LeadTest1")
    LeadTest1.isMeasuredIn.append(mlperLitter)
    LeadTest1.relatesToProperty.append(saref4water.Lead)
    LeadTest1.hasTimestamp.append(datetime.strptime("2022-03-06T21:01:30", '%Y-%m-%dT%H:%M:%S'))
    LeadTest1.hasValue.append(0.31)

    ZincTest1 = saref.Measurement("ZincTest1")
    Zinc = saref4water.ChemicalProperty("Zinc")
    Zinc.hasName.append("Zinc")
    Zinc.hasDescription.append("Zinc")
    ZincTest1.isMeasuredIn.append(mlperLitter)
    ZincTest1.relatesToProperty.append(Zinc)
    ZincTest1.hasTimestamp.append(datetime.strptime("2022-03-06T21:01:30", '%Y-%m-%dT%H:%M:%S'))
    ZincTest1.hasValue.append(0.19)

    CooperTest1 = saref.Measurement("CooperTest1")
    CooperTest1.isMeasuredIn.append(mlperLitter)
    CooperTest1.relatesToProperty.append(saref4water.Copper)
    CooperTest1.hasTimestamp.append(datetime.strptime("2022-03-06T21:01:30", '%Y-%m-%dT%H:%M:%S'))
    CooperTest1.hasValue.append(0.31)

    CadmiumTest1 = saref.Measurement("CadmiumTest1")
    CadmiumTest1.isMeasuredIn.append(mlperLitter)
    CadmiumTest1.relatesToProperty.append(saref4water.Cadmium)
    CadmiumTest1.hasTimestamp.append(datetime.strptime("2022-03-06T21:01:30", '%Y-%m-%dT%H:%M:%S'))
    CadmiumTest1.hasValue.append(0.16)

    centralisedTreatment.hasMeasurement.append(phMeasurementTest1)
    centralisedTreatment.hasMeasurement.append(totalCODTest1)
    centralisedTreatment.hasMeasurement.append(filteredCODTest1)
    centralisedTreatment.hasMeasurement.append(BODTest1)
    centralisedTreatment.hasMeasurement.append(FilteredBODTest1)
    centralisedTreatment.hasMeasurement.append(TOCTEst1)
    centralisedTreatment.hasMeasurement.append(TurbidityTest1)
    centralisedTreatment.hasMeasurement.append(TKNTest1)
    centralisedTreatment.hasMeasurement.append(NH3Test1)
    centralisedTreatment.hasMeasurement.append(NH4Test1)
    centralisedTreatment.hasMeasurement.append(TotalNitrogenTest1)
    centralisedTreatment.hasMeasurement.append(TPTest1)
    centralisedTreatment.hasMeasurement.append(OPTest1)
    centralisedTreatment.hasMeasurement.append(TDSTest1)
    centralisedTreatment.hasMeasurement.append(AlkalinityTest1)
    centralisedTreatment.hasMeasurement.append(FatOilGreaseTest1)
    centralisedTreatment.hasMeasurement.append(ConductivityTest1)
    centralisedTreatment.hasMeasurement.append(SO4Test1)
    centralisedTreatment.hasMeasurement.append(SilicaSolubleTest1)
    centralisedTreatment.hasMeasurement.append(eColiTest1)
    centralisedTreatment.hasMeasurement.append(LegionaleaSSPTest1)
    centralisedTreatment.hasMeasurement.append(CampylobacterSPPTest1)
    centralisedTreatment.hasMeasurement.append(SalmonellaSPPTest1)
    centralisedTreatment.hasMeasurement.append(PseudomonasSPPTest1)
    centralisedTreatment.hasMeasurement.append(StaphylococcusAureusTest1)
    centralisedTreatment.hasMeasurement.append(TotalCountTest1)
    centralisedTreatment.hasMeasurement.append(TotalColiformTest1)
    centralisedTreatment.hasMeasurement.append(NickelTest1)
    centralisedTreatment.hasMeasurement.append(LeadTest1)
    centralisedTreatment.hasMeasurement.append(ZincTest1)
    centralisedTreatment.hasMeasurement.append(CooperTest1)
    centralisedTreatment.hasMeasurement.append(CadmiumTest1)

    pilotPlantTreatment = wsisSchema.ResourceProducer("PilotPlantTreatment")
    pilotPlantTreatment.hasName.append("Pilot Treatment Plant")
    DAF.usesTechnology.append(pilotPlantTreatment)

    holdingTank = wsisSchema.Technology("HoldingTank")
    holdingTank.hasName.append("Holding Tank")
    pilotPlantTreatment.usesTechnology.append(holdingTank)
    holdingTank.canProcess.append(waterDAF)
    waterHoldingTank = saref4water.Water("waterHoldingTank")
    holdingTank.generates.append(waterHoldingTank)

    membraneBioReactor = wsisSchema.Technology("MembraneBioReactor")
    membraneBioReactor.hasName.append("Membrane Bioreactor")
    holdingTank.usesTechnology.append(membraneBioReactor)
    membraneBioReactor.canProcess.append(waterHoldingTank)

    waterMembraneBioReactor = saref4water.Water("waterMembraneBioReactor")
    membraneBioReactor.generates.append(waterMembraneBioReactor)

    WAS = wsisSchema.SolidMaterial("WAS")
    membraneBioReactor.generates.append(WAS)
    RAS = wsisSchema.SolidMaterial("RAS")
    membraneBioReactor.generates.append(RAS)

    membraneBioReactor.canProcess.append(RAS)

    ionExchange = wsisSchema.Technology("IonExchange")
    ionExchange.hasName.append("Ion Exchange")
    membraneBioReactor.usesTechnology.append(ionExchange)
    ionExchange.canProcess.append(waterMembraneBioReactor)

    waterIonExchange = saref4water.Water("waterIonExchange")
    ionExchange.generates.append(waterIonExchange)
    wasteIonExchange = wsisSchema.SolidMaterial("WasteIonExchange")
    ionExchange.generates.append(wasteIonExchange)

    UVH2O2 = wsisSchema.Technology("UVH2O2")
    UVH2O2.hasName.append("UVH2O2")
    ionExchange.usesTechnology.append(UVH2O2)
    UVH2O2.canProcess.append(waterIonExchange)

    treatedWater = saref4water.Water("TreatedWater")
    UVH2O2.generates.append(treatedWater)

    agricola.canProcess.append(treatedWater)

    return wsisSchema


if __name__ == '__main__':
    onto_path.append("./ontologies/")
    wsisSchema = get_ontology("wsis.owl").load()
    print (list(wsisSchema.classes()))

    # CS1 Implementation
    #cs1_iparkdow = CS1_IparkDOW(wsisSchema)
    #cs1_iparkdow.save(file="./cs-ontology/cs-population/CS1-IParcDOW/aq-iparkdow.rdf")

    #cs1_dow_bohlen = CS1_DOW_Bohlen(wsisSchema)
    #cs1_dow_bohlen.save(file="./cs-ontology/cs-population/CS1-IParcDOW/aq-dow-bohlen.rdf")

    #CS2 Implementation
    #cs2_solvay = CS2_Solvay(wsisSchema)
    #cs2_solvay.save(file="./cs-ontology/cs-population/CS2-Solvay/aq-solvay.rdf")

    # CS3-ANTWERP HARBOUR AND ALBERT CANAL Implementation
    cs3_antwerpHarbour = CS3_AntwerpHarbour(wsisSchema)
    cs3_antwerpHarbour.save(file="cs-ontology/cs-population/CS3_Antewerp/aq-antwerp-harbour.rdf")
    cs3_antwerpHarbourGraph = default_world.as_rdflib_graph()
    cs3_antwerpHarbourGraph.serialize(destination='cs-ontology/cs-population/CS3_Antewerp/aq-antwerp-harbour_2.ttl', format='ttl')


    # CS3-BASF
    #cs3_BASF = CS3_BASF(wsisSchema)
    #cs3_BASF.save(file="cs-ontology/cs-population/CS3_Antewerp/aq-BASF.rdf")

    #agricolaInstances = CS5_agricola_instances (wsisSchema)
    #agricolaInstances.save(file="aq-agricola.rdf")

    #CS6- TUPRAS
    #onto = CS6_TUPRAS(wsisSchema)
    #onto.save(file="./cs-ontology/cs-population/CS6-Tupras/aq-Tupras.rdf")

