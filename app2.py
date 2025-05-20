import streamlit as st
import time
from datetime import datetime, timedelta
import random

# Set page configuration
st.set_page_config(
    page_title="BoardingPass AI Data Processing Demo",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Define some styling
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        font-weight: bold;
        color: #1E3A8A;
        margin-bottom: 1rem;
    }
    .section-header {
        font-size: 1.8rem;
        font-weight: bold;
        color: #1E3A8A;
        margin-top: 2rem;
        margin-bottom: 1rem;
    }
    .step-header {
        font-size: 1.3rem;
        font-weight: bold;
        color: #1E3A8A;
        margin-top: 1rem;
    }
    .info-box {
        background-color: #F0F7FF;
        padding: 1rem;
        border-radius: 0.5rem;
        border-left: 0.5rem solid #3B82F6;
        margin-bottom: 1rem;
    }
    .success-box {
        background-color: #F0FFF4;
        padding: 1rem;
        border-radius: 0.5rem;
        border-left: 0.5rem solid #10B981;
        margin-bottom: 1rem;
    }
    .warning-box {
        background-color: #FFFBEB;
        padding: 1rem;
        border-radius: 0.5rem;
        border-left: 0.5rem solid #F59E0B;
        margin-bottom: 1rem;
    }
    .error-box {
        background-color: #FEF2F2;
        padding: 1rem;
        border-radius: 0.5rem;
        border-left: 0.5rem solid #EF4444;
        margin-bottom: 1rem;
    }
    .highlight {
        background-color: #FFFF00;
        padding: 0.2rem;
    }
    .code-box {
        background-color: #1F2937;
        color: #F9FAFB;
        padding: 1rem;
        border-radius: 0.5rem;
        font-family: monospace;
        margin-bottom: 1rem;
        overflow-x: auto;
    }
    .pipeline-step {
        background-color: #EFF6FF;
        padding: 1rem;
        border-radius: 0.5rem;
        margin-bottom: 1rem;
        border: 1px solid #DBEAFE;
    }
    .step-animation {
        height: 5px;
        background-color: #3B82F6;
        margin-bottom: 1rem;
        width: 0%;
    }
    div[data-testid="stSidebar"] {
        background-color: #F8FAFC;
    }
</style>
""", unsafe_allow_html=True)

# Main title
st.markdown('<div class="main-header">BoardingPass AI Data Processing Demonstration</div>', unsafe_allow_html=True)

# Sidebar content
with st.sidebar:
    st.markdown("## Demo Settings")
    
    data_source = st.selectbox(
        "Select Data Source Format",
        ["XML", "CSV", "Excel-like", "JSON"]
    )
    
    source_system = st.selectbox(
        "Select Source System",
        ["Northern Trust", "State Street", "Vanguard", "Fidelity", "RPAG"]
    )
    
    abnormality_level = st.slider(
        "Data Abnormality Level",
        min_value=0,
        max_value=100,
        value=50,
        help="Higher values create more schema and data quality issues"
    )
    
    show_technical = st.checkbox("Show Technical Details", value=False)
    
    st.markdown("---")
    st.markdown("### About This Demo")
    st.markdown("""
    This dashboard demonstrates the AI-powered data processing capabilities of the enhanced BoardingPass platform:

    1. **Intelligent Pipeline Orchestration** - Dynamically selects the appropriate processing workflow
    
    2. **Adaptive Schema Recognition** - Automatically maps fields regardless of naming or order
    
    3. **Data Quality Enhancement** - Standardizes values and corrects errors

    Use the controls above to simulate different data scenarios.
    """)

# Sample data for demonstration
sample_data = {
    "XML": f"""<RetirementPlan>
  <PlanID>P{random.randint(10000, 99999)}</PlanID>
  <PlanName>Retirement Plan {random.choice(['A', 'B', 'C'])}</PlanName>
  <PlanSponsor>{random.choice(['Acme', 'GlobalTech', 'Summit'])} {random.choice(['Inc', 'LLC', 'Corp'])}</PlanSponsor>
  <FeeClass>Class {random.choice(['A', 'B', 'C'])}</FeeClass>
  <CUSIP>{random.randint(100000000, 999999999)}</CUSIP>
  <FundName>{random.choice(['Growth', 'Value', 'Income'])} Fund</FundName>
  <AUM>${random.randint(1000000, 9999999)}</AUM>
</RetirementPlan>""",
    
    "CSV": f"""Plan ID,Plan Name,Plan Sponsor,Fee Class,CUSIP,Fund Name,AUM
P{random.randint(10000, 99999)},Retirement Plan {random.choice(['A', 'B', 'C'])},{random.choice(['Acme', 'GlobalTech', 'Summit'])} {random.choice(['Inc', 'LLC', 'Corp'])},Class {random.choice(['A', 'B', 'C'])},{random.randint(100000000, 999999999)},{random.choice(['Growth', 'Value', 'Income'])} Fund,${random.randint(1000000, 9999999)}""",
    
    "Excel-like": f"""Report Generated: {datetime.now().strftime('%m/%d/%Y %H:%M:%S')},,,,,,
Source: {source_system},,,,,,
,,,,,,
Plan ID,Plan Name,Plan Sponsor,Fee Class,CUSIP,Fund Name,AUM
P{random.randint(10000, 99999)},Retirement Plan {random.choice(['A', 'B', 'C'])},{random.choice(['Acme', 'GlobalTech', 'Summit'])} {random.choice(['Inc', 'LLC', 'Corp'])},Class {random.choice(['A', 'B', 'C'])},{random.randint(100000000, 999999999)},{random.choice(['Growth', 'Value', 'Income'])} Fund,${random.randint(1000000, 9999999)}""",
    
    "JSON": f"""{{
  "PlanID": "P{random.randint(10000, 99999)}",
  "PlanName": "Retirement Plan {random.choice(['A', 'B', 'C'])}",
  "PlanSponsor": "{random.choice(['Acme', 'GlobalTech', 'Summit'])} {random.choice(['Inc', 'LLC', 'Corp'])}",
  "FeeClass": "Class {random.choice(['A', 'B', 'C'])}",
  "CUSIP": "{random.randint(100000000, 999999999)}",
  "FundName": "{random.choice(['Growth', 'Value', 'Income'])} Fund",
  "AUM": "${random.randint(1000000, 9999999)}"
}}"""
}

# Use the selected data format
raw_data = sample_data[data_source]

# Display the data pipeline process
st.markdown('<div class="section-header">Data Processing Pipeline</div>', unsafe_allow_html=True)

# Two columns layout
col1, col2 = st.columns([3, 2])

with col1:
    st.markdown('<div class="step-header">Source Data</div>', unsafe_allow_html=True)
    st.markdown('<div class="info-box">The following data was received from the source system:</div>', unsafe_allow_html=True)
    
    if data_source == "XML":
        st.code(raw_data, language="xml")
    elif data_source == "JSON":
        st.code(raw_data, language="json")
    else:
        st.code(raw_data)

with col2:
    st.markdown('<div class="step-header">Source Information</div>', unsafe_allow_html=True)
    st.markdown(f"""
    <div class="info-box">
        <strong>Source System:</strong> {source_system}<br>
        <strong>File Format:</strong> {data_source}<br>
        <strong>Received:</strong> {datetime.now().strftime('%m/%d/%Y %H:%M:%S')}<br>
        <strong>File Size:</strong> {len(raw_data)} bytes
    </div>
    """, unsafe_allow_html=True)

# Step 1: Intelligent Pipeline Orchestration
st.markdown('<div class="section-header">Step 1: Intelligent Pipeline Orchestration</div>', unsafe_allow_html=True)
st.markdown("""
<div class="info-box">
The AI system analyzes the incoming data to determine file format and source, then dynamically selects the appropriate processing workflow.
</div>
""", unsafe_allow_html=True)

orchestration_col1, orchestration_col2 = st.columns([3, 2])

with orchestration_col1:
    # Show a visual representation of the pipeline orchestration
    st.markdown('<div class="pipeline-step">File Type Detection</div>', unsafe_allow_html=True)
    file_type_progress = st.progress(0)
    st.markdown('<div class="pipeline-step">Source System Analysis</div>', unsafe_allow_html=True)
    source_analysis_progress = st.progress(0)
    st.markdown('<div class="pipeline-step">Workflow Selection</div>', unsafe_allow_html=True)
    workflow_selection_progress = st.progress(0)
    
    # Simulate processing
    for i in range(101):
        file_type_progress.progress(i)
        if i > 30:
            source_analysis_progress.progress(min(100, (i-30)*1.5))
        if i > 70:
            workflow_selection_progress.progress(min(100, (i-70)*3.5))
        time.sleep(0.01)

with orchestration_col2:
    st.markdown('<div class="step-header">Pipeline Decision</div>', unsafe_allow_html=True)
    
    # Generate pipeline decision based on source and format
    pipeline_decision = {
        "XML": {
            "Northern Trust": "Northern Trust XML Ingestion Pipeline",
            "State Street": "State Street XML Processing Flow",
            "Vanguard": "Vanguard Data Integration Pipeline",
            "Fidelity": "Fidelity XML Standard Processor",
            "RPAG": "RPAG Multi-format Ingestion Pipeline"
        },
        "CSV": {
            "Northern Trust": "Northern Trust CSV Standard Flow",
            "State Street": "State Street Tabular Data Pipeline",
            "Vanguard": "Vanguard CSV Integration Flow",
            "Fidelity": "Fidelity Structured Data Pipeline",
            "RPAG": "RPAG Multi-format Ingestion Pipeline"
        },
        "Excel-like": {
            "Northern Trust": "Northern Trust Excel Processor",
            "State Street": "State Street Workbook Pipeline",
            "Vanguard": "Vanguard Excel Integration Flow",
            "Fidelity": "Fidelity Spreadsheet Processor",
            "RPAG": "RPAG Multi-format Ingestion Pipeline"
        },
        "JSON": {
            "Northern Trust": "Northern Trust API Processor",
            "State Street": "State Street JSON Pipeline",
            "Vanguard": "Vanguard API Integration Flow",
            "Fidelity": "Fidelity JSON Standard Processor",
            "RPAG": "RPAG Multi-format Ingestion Pipeline"
        }
    }
    
    selected_pipeline = pipeline_decision[data_source][source_system]
    
    st.markdown(f"""
    <div class="success-box">
        <strong>Selected Workflow:</strong> {selected_pipeline}<br><br>
        <strong>Processing Steps:</strong>
        <ul>
            <li>Parse {data_source} format using specialized {source_system} parser</li>
            <li>Apply {source_system}-specific validation rules</li>
            <li>Use historical patterns from {source_system} for enhanced processing</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    
    if show_technical:
        st.markdown('<div class="code-box">AI Score: Pipeline selection confidence 93%\nSelected parser: specialized_{}_processor\nValidation ruleset: {}_rules_v3</div>'.format(
            data_source.lower(), source_system.lower().replace(" ", "_")), unsafe_allow_html=True)

# Step 2: Adaptive Schema Recognition
st.markdown('<div class="section-header">Step 2: Adaptive Schema Recognition</div>', unsafe_allow_html=True)
st.markdown("""
<div class="info-box">
The AI system automatically identifies data fields and maps them to the standard schema, regardless of naming conventions or field order.
</div>
""", unsafe_allow_html=True)

# Field mapping demonstration
mapping_col1, mapping_col2 = st.columns([3, 2])

with mapping_col1:
    st.markdown('<div class="step-header">Field Mapping</div>', unsafe_allow_html=True)
    
    # Create mapping data based on source system
    if source_system == "Northern Trust":
        mapping_data = [
            {"Standard Field": "plan_id", "Source Field": "PlanIdentifier", "Confidence": 0.95, "Description": "Plan unique identifier"},
            {"Standard Field": "plan_name", "Source Field": "PlanName", "Confidence": 0.98, "Description": "Plan name"},
            {"Standard Field": "sponsor_name", "Source Field": "SponsorName", "Confidence": 0.92, "Description": "Plan sponsor"},
            {"Standard Field": "fee_class", "Source Field": "ShareClass", "Confidence": 0.87, "Description": "Fee class"},
            {"Standard Field": "cusip", "Source Field": "CUSIP", "Confidence": 0.97, "Description": "CUSIP identifier"},
            {"Standard Field": "ticker", "Source Field": "Not Found", "Confidence": 0.0, "Description": "Ticker symbol"},
            {"Standard Field": "fund_name", "Source Field": "FundName", "Confidence": 0.94, "Description": "Fund name"},
            {"Standard Field": "aum", "Source Field": "AssetsUnderManagement", "Confidence": 0.91, "Description": "Assets under management"},
        ]
    elif source_system == "State Street":
        mapping_data = [
            {"Standard Field": "plan_id", "Source Field": "SSPlanID", "Confidence": 0.93, "Description": "Plan unique identifier"},
            {"Standard Field": "plan_name", "Source Field": "PlanTitle", "Confidence": 0.89, "Description": "Plan name"},
            {"Standard Field": "sponsor_name", "Source Field": "ClientName", "Confidence": 0.86, "Description": "Plan sponsor"},
            {"Standard Field": "fee_class", "Source Field": "FeeClass", "Confidence": 0.98, "Description": "Fee class"},
            {"Standard Field": "cusip", "Source Field": "CUSIP", "Confidence": 0.97, "Description": "CUSIP identifier"},
            {"Standard Field": "ticker", "Source Field": "TickerSymbol", "Confidence": 0.96, "Description": "Ticker symbol"},
            {"Standard Field": "fund_name", "Source Field": "InvestmentName", "Confidence": 0.88, "Description": "Fund name"},
            {"Standard Field": "aum", "Source Field": "TotalAssets", "Confidence": 0.91, "Description": "Assets under management"},
        ]
    else:
        mapping_data = [
            {"Standard Field": "plan_id", "Source Field": "PlanID", "Confidence": 0.97, "Description": "Plan unique identifier"},
            {"Standard Field": "plan_name", "Source Field": "PlanName", "Confidence": 0.98, "Description": "Plan name"},
            {"Standard Field": "sponsor_name", "Source Field": "PlanSponsor", "Confidence": 0.96, "Description": "Plan sponsor"},
            {"Standard Field": "fee_class", "Source Field": "FeeClass", "Confidence": 0.95, "Description": "Fee class"},
            {"Standard Field": "cusip", "Source Field": "CUSIP", "Confidence": 0.97, "Description": "CUSIP identifier"},
            {"Standard Field": "ticker", "Source Field": "Ticker", "Confidence": 0.94, "Description": "Ticker symbol"},
            {"Standard Field": "fund_name", "Source Field": "FundName", "Confidence": 0.97, "Description": "Fund name"},
            {"Standard Field": "aum", "Source Field": "AUM", "Confidence": 0.98, "Description": "Assets under management"},
        ]
    
    # Display as a table
    st.markdown("""
    | Standard Field | Source Field | Confidence | Description |
    |---------------|--------------|------------|-------------|
    """)
    
    for field in mapping_data:
        confidence_color = ""
        if field["Confidence"] > 0.9:
            confidence_color = "🟢"
        elif field["Confidence"] > 0.8:
            confidence_color = "🟡"
        elif field["Confidence"] > 0:
            confidence_color = "🔴"
        else:
            confidence_color = "⚪"
            
        confidence_pct = f"{field['Confidence']*100:.0f}%" if field["Confidence"] > 0 else "N/A"
        
        st.markdown(f"""
        | {field["Standard Field"]} | {field["Source Field"]} | {confidence_pct} {confidence_color} | {field["Description"]} |
        """)

with mapping_col2:
    st.markdown('<div class="step-header">AI Schema Recognition</div>', unsafe_allow_html=True)
    
    # Calculate mapping quality metrics
    fields_mapped = len([m for m in mapping_data if m["Source Field"] != "Not Found"])
    fields_missed = len(mapping_data) - fields_mapped
    mapping_quality = sum([m["Confidence"] for m in mapping_data]) / len(mapping_data)
    
    st.markdown(f"""
    <div class="success-box">
        <strong>Mapping Quality:</strong> {mapping_quality:.0%}<br>
        <strong>Fields Mapped:</strong> {fields_mapped} of {len(mapping_data)}<br>
        <strong>Fields Not Found:</strong> {fields_missed}<br><br>
        
        <strong>AI Reasoning:</strong><br>
        Based on historical patterns from {source_system} data and lexical analysis, 
        the AI has determined field mappings with {mapping_quality:.0%} confidence.
    </div>
    """, unsafe_allow_html=True)
    
    if show_technical:
        st.markdown(f"""
        <div class="code-box">
        Schema Recognition Methods:
        - Pattern matching: 65%
        - Historical mapping data: 20%
        - ML-based field prediction: 15%
        
        Model: field_mapping_v2.3
        Confidence threshold: 0.75
        </div>
        """, unsafe_allow_html=True)

# Step 3: Data Quality Enhancement
st.markdown('<div class="section-header">Step 3: Data Quality Enhancement</div>', unsafe_allow_html=True)
st.markdown("""
<div class="info-box">
The AI system standardizes data values, fixes inconsistencies, and fills missing values where possible.
</div>
""", unsafe_allow_html=True)

quality_col1, quality_col2 = st.columns([3, 2])

with quality_col1:
    st.markdown('<div class="step-header">Data Standardization</div>', unsafe_allow_html=True)
    
    # Create a demonstration of data standardization
    quality_issues = [
        {
            "Field": "Fee Class",
            "Original Value": "Class A",
            "Standardized Value": "A",
            "Rule Applied": "Remove 'Class' prefix and standardize case"
        },
        {
            "Field": "Date",
            "Original Value": "05/15/2024",
            "Standardized Value": "2024-05-15",
            "Rule Applied": "Standardize to YYYY-MM-DD format"
        },
        {
            "Field": "AUM",
            "Original Value": "$12,345,678",
            "Standardized Value": "$12,345,678.00",
            "Rule Applied": "Standardize currency format"
        }
    ]
    
    # Display as a table
    st.markdown("""
    | Field | Original Value | Standardized Value | Rule Applied |
    |-------|---------------|-------------------|-------------|
    """)
    
    for issue in quality_issues:
        st.markdown(f"""
        | {issue["Field"]} | {issue["Original Value"]} | {issue["Standardized Value"]} | {issue["Rule Applied"]} |
        """)

with quality_col2:
    st.markdown('<div class="step-header">Quality Enhancement Results</div>', unsafe_allow_html=True)
    
    # Quality stats
    quality_improvements = len(quality_issues)
    confidence_score = 0.92
    
    st.markdown(f"""
    <div class="success-box">
        <strong>Quality Improvements:</strong> {quality_improvements} fields standardized<br>
        <strong>Confidence Score:</strong> {confidence_score:.0%}<br><br>
        
        <strong>AI Processing:</strong><br>
        The system has applied {source_system}-specific standardization rules
        and enterprise data quality standards to ensure consistency.
    </div>
    """, unsafe_allow_html=True)
    
    if show_technical:
        st.markdown(f"""
        <div class="code-box">
        Data Quality Methods:
        - Rule-based standardization: 70%
        - Pattern-based correction: 20%
        - ML-based data repair: 10%
        
        Applied quality rules: 
        - date_standardization
        - currency_formatting
        - case_normalization
        - field_format_correction
        </div>
        """, unsafe_allow_html=True)

# Final Result
st.markdown('<div class="section-header">Final Processed Data</div>', unsafe_allow_html=True)

# Display standardized data
st.markdown("""
| Plan ID | Plan Name | Plan Sponsor | Fee Class | CUSIP | Fund Name | Assets Under Management | Effective Date |
|---------|-----------|--------------|-----------|-------|-----------|------------------------|----------------|
""")

st.markdown(f"""
| P{random.randint(10000, 99999)} | Retirement Plan {random.choice(['A', 'B', 'C'])} | {random.choice(['Acme', 'GlobalTech', 'Summit'])} {random.choice(['Inc', 'LLC', 'Corp'])} | {random.choice(['A', 'B', 'C'])} | {random.randint(100000000, 999999999)} | {random.choice(['Growth', 'Value', 'Income'])} Fund | ${random.randint(1000000, 9999999)}.00 | {random.randint(2020, 2024)}-{random.randint(1, 12):02d}-{random.randint(1, 28):02d} |
""")

# Summary and metrics
st.markdown('<div class="section-header">Process Summary</div>', unsafe_allow_html=True)

summary_col1, summary_col2, summary_col3 = st.columns(3)

with summary_col1:
    st.markdown("""
    <div class="info-box">
        <h3 style="text-align: center;">Pipeline Orchestration</h3>
        <div style="text-align: center; font-size: 2rem; margin: 1rem 0;">✓</div>
        <p style="text-align: center;">Correctly identified source system and format</p>
        <p style="text-align: center;">Applied optimal processing workflow</p>
    </div>
    """, unsafe_allow_html=True)

with summary_col2:
    st.markdown("""
    <div class="info-box">
        <h3 style="text-align: center;">Schema Recognition</h3>
        <div style="text-align: center; font-size: 2rem; margin: 1rem 0;">🔄</div>
        <p style="text-align: center;">Successfully mapped fields despite variations</p>
        <p style="text-align: center;">Applied machine learning to handle unknown formats</p>
    </div>
    """, unsafe_allow_html=True)

with summary_col3:
    st.markdown("""
    <div class="info-box">
        <h3 style="text-align: center;">Data Quality</h3>
        <div style="text-align: center; font-size: 2rem; margin: 1rem 0;">⚙️</div>
        <p style="text-align: center;">Standardized formats across all fields</p>
        <p style="text-align: center;">Applied industry-specific data rules</p>
    </div>
    """, unsafe_allow_html=True)

# Process metrics
st.markdown('<div class="step-header">Process Metrics</div>', unsafe_allow_html=True)

metrics_col1, metrics_col2, metrics_col3, metrics_col4 = st.columns(4)

with metrics_col1:
    st.metric(
        label="Processing Time", 
        value=f"{random.uniform(0.2, 1.5):.2f}s",
        delta="-75%"
    )

with metrics_col2:
    st.metric(
        label="Fields Mapped", 
        value=f"{fields_mapped}/{len(mapping_data)}",
        delta="Auto-detected"
    )

with metrics_col3:
    st.metric(
        label="Quality Score", 
        value=f"{random.uniform(85, 98):.0f}%",
        delta="+12%"
    )

with metrics_col4:
    st.metric(
        label="Manual Effort Saved", 
        value=f"{random.uniform(10, 30):.0f} min",
        delta="per file"
    )

# Technical explanation section
if show_technical:
    st.markdown('<div class="section-header">Technical Details</div>', unsafe_allow_html=True)
    
    with st.expander("AI Processing Pipeline Technical Documentation"):
        st.markdown("""
        ## Intelligent Pipeline Orchestration
        
        The pipeline orchestration component uses a combination of rule-based and ML approaches:
        
        1. **File Format Detection**:
           - Content-based heuristics examine file structure
           - Character frequency analysis identifies delimiter patterns
           - Trained ML model recognizes file signatures
        
        2. **Source System Analysis**:
           - Pattern recognition against known source templates
           - Fingerprinting based on field naming conventions
           - Historical pattern matching from previous ingestions
        
        3. **Workflow Selection**:
           - Decision tree model with 94% accuracy
           - Optimized for specific source system quirks
           - Self-optimizing based on processing outcomes
        
        ## Adaptive Schema Recognition
        
        The schema recognition component maps incoming fields to the standard schema:
        
        1. **Field Identification**:
           - Lexical analysis of field names
           - Regular expression pattern matching
           - Semantic similarity using word embeddings
        
        2. **Mapping Confidence Calculation**:
           - Combined score from multiple methods
           - Contextual clues from field values
           - Prior mapping history weighting
        
        3. **Field Value Analysis**:
           - Statistical profiling of value distributions
           - Data type inference and validation
           - Format pattern recognition
        
        ## Data Quality Enhancement
        
        The data quality component standardizes and corrects data:
        
        1. **Standardization Rules**:
           - Format normalization (dates, currency, IDs)
           - Value cleaning (whitespace, case, prefixes)
           - Unit conversion where applicable
        
        2. **Anomaly Detection**:
           - Statistical outlier detection
           - Industry-specific validation rules
           - Cross-field consistency checks
        
        3. **Machine Learning Corrections**:
           - Value prediction for missing data
           - Auto-correction of common errors
           - Pattern-based data repair
        """)

# Key takeaways section
st.markdown('<div class="section-header">Key Takeaways</div>', unsafe_allow_html=True)

takeaways_col1, takeaways_col2 = st.columns(2)

with takeaways_col1:
    st.markdown("""
    <div class="success-box">
        <h3>Intelligent Pipeline Orchestration</h3>
        <ul>
            <li><strong>Identifies file formats and sources automatically</strong> - no need for manual classification</li>
            <li><strong>Selects optimal processing workflow</strong> based on source system characteristics</li>
            <li><strong>Adapts dynamically to changes</strong> in source formats and systems</li>
            <li><strong>Learns from processing history</strong> to continuously improve accuracy</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="success-box">
        <h3>Business Benefits</h3>
        <ul>
            <li><strong>90% reduction in manual data processing</strong> across the retirement value chain</li>
            <li><strong>75% faster integration</strong> of new data sources and partners</li>
            <li><strong>99% data accuracy</strong> through AI-powered quality enhancement</li>
            <li><strong>Unified data model</strong> across all retirement ecosystem participants</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

with takeaways_col2:
    st.markdown("""
    <div class="success-box">
        <h3>Adaptive Schema Recognition</h3>
        <ul>
            <li><strong>Maps fields automatically</strong> regardless of naming or position</li>
            <li><strong>Handles unknown formats</strong> without predefined mapping rules</li>
            <li><strong>Provides confidence scores</strong> for mapping decisions</li>
            <li><strong>Improves over time</strong> through machine learning from corrections</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="success-box">
        <h3>Data Quality Enhancement</h3>
        <ul>
            <li><strong>Standardizes values</strong> across different source systems</li>
            <li><strong>Corrects common errors</strong> using industry-specific rules</li>
            <li><strong>Fills missing data</strong> using predictive models where appropriate</li>
            <li><strong>Ensures consistency</strong> across the entire retirement data ecosystem</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #6B7280; font-size: 0.8rem;">
    Great Gray AI Data Processing Demonstration | Created for Director of Data Science and AI | May 20, 2025
</div>
""", unsafe_allow_html=True)
