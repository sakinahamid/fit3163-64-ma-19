import os
from flask import Flask, request, render_template, redirect, url_for

from werkzeug.utils import secure_filename

app = Flask(__name__)


uploads_dir = os.path.join(app.instance_path, 'uploads')
os.makedirs(uploads_dir, exist_ok=True)


@app.route('/api/upload', methods=['POST'])
def upload_file():
    file = request.files['file']
    file.save(os.path.join(uploads_dir, secure_filename(file.filename)))

    # save each "charts" file
    for file in request.files.getlist('charts'):
        file.save(os.path.join(uploads_dir, secure_filename(file.name)))

    return "OK"


@app.route('/data')
def react_link():
    return {
        "nodes": [
            {"id": "Germany", "name": "Germany", "val": 1, "group": 1},
            {
                "id": "Springer Nature",
                "name": "Springer Nature",
                "val": 1,
                "group": 1
            },
            {
                "id": "Germany,Springer",
                "name": "Germany,Springer",
                "val": 1,
                "group": 1
            },
            {"id": "Springer", "name": "Springer", "val": 1, "group": 1},
            {"id": "patients", "name": "patients", "val": 45, "group": 1},
            {
                "id": "acute respiratory disease",
                "name": "acute respiratory disease",
                "val": 2,
                "group": 1
            },
            {"id": "aim", "name": "aim", "val": 10, "group": 1},
            {
                "id": "patients,acute respiratory disease",
                "name": "patients,acute respiratory disease",
                "val": 1,
                "group": 1
            },
            {"id": "COVID 19", "name": "COVID 19", "val": 12, "group": 1},
            {"id": "China", "name": "China", "val": 4, "group": 1},
            {"id": "Wuhan", "name": "Wuhan", "val": 6, "group": 1},
            {"id": "Methods", "name": "Methods", "val": 12, "group": 1},
            {
                "id": "18F FDG PET CT results",
                "name": "18F FDG PET CT results",
                "val": 6,
                "group": 1
            },
            {"id": "We", "name": "We", "val": 4, "group": 1},
            {"id": "four patients", "name": "four patients", "val": 2, "group": 1},
            {"id": "outbreak", "name": "outbreak", "val": 10, "group": 1},
            {
                "id": "still unrecognized",
                "name": "still unrecognized",
                "val": 2,
                "group": 1
            },
            {
                "id": "when still unrecognized",
                "name": "when still unrecognized",
                "val": 2,
                "group": 1
            },
            {"id": "unrecognized", "name": "unrecognized", "val": 2, "group": 1},
            {
                "id": "when unrecognized",
                "name": "when unrecognized",
                "val": 2,
                "group": 1
            },
            {"id": "virus", "name": "virus", "val": 2, "group": 1},
            {"id": "unknown", "name": "unknown", "val": 9, "group": 1},
            {
                "id": "virus,infectivity",
                "name": "virus,infectivity",
                "val": 7,
                "group": 1
            },
            {"id": "imaging", "name": "imaging", "val": 12, "group": 1},
            {"id": "diagnosis", "name": "diagnosis", "val": 30, "group": 1},
            {
                "id": "imaging,findings",
                "name": "imaging,findings",
                "val": 12,
                "group": 1
            },
            {
                "id": "diagnosis of COVID 19",
                "name": "diagnosis of COVID 19",
                "val": 4,
                "group": 1
            },
            {
                "id": "ground glass opacities",
                "name": "ground glass opacities",
                "val": 6,
                "group": 1
            },
            {
                "id": "peripheral ground glass opacities",
                "name": "peripheral ground glass opacities",
                "val": 1,
                "group": 1
            },
            {"id": "peripheral", "name": "peripheral", "val": 8, "group": 1},
            {"id": "lesions", "name": "lesions", "val": 20, "group": 1},
            {"id": "18F FDG uptake", "name": "18F FDG uptake", "val": 2, "group": 1},
            {"id": "uptake", "name": "uptake", "val": 8, "group": 1},
            {
                "id": "high 18F FDG uptake",
                "name": "high 18F FDG uptake",
                "val": 2,
                "group": 1
            },
            {"id": "tropism", "name": "tropism", "val": 2, "group": 1},
            {"id": "inated disease", "name": "inated disease", "val": 5, "group": 1},
            {"id": "absent", "name": "absent", "val": 13, "group": 1},
            {"id": "disease", "name": "disease", "val": 4, "group": 1},
            {"id": "pulmonary", "name": "pulmonary", "val": 2, "group": 1},
            {
                "id": "pulmonary,tropism",
                "name": "pulmonary,tropism",
                "val": 2,
                "group": 1
            },
            {"id": "pilot data", "name": "pilot data", "val": 52, "group": 1},
            {"id": "light", "name": "light", "val": 4, "group": 1},
            {
                "id": "potential utility of imaging technique in diagnosis",
                "name": "potential utility of imaging technique in diagnosis",
                "val": 2,
                "group": 1
            },
            {
                "id": "imaging technique",
                "name": "imaging technique",
                "val": 5,
                "group": 1
            },
            {"id": "clinical", "name": "clinical", "val": 14, "group": 1},
            {
                "id": "differential diagnosis",
                "name": "differential diagnosis",
                "val": 4,
                "group": 1
            },
            {
                "id": "potential utility in diagnosis",
                "name": "potential utility in diagnosis",
                "val": 4,
                "group": 1
            },
            {
                "id": "potential clinical utility in differential diagnosis",
                "name": "potential clinical utility in differential diagnosis",
                "val": 1,
                "group": 1
            },
            {
                "id": "clinical,differential diagnosis",
                "name": "clinical,differential diagnosis",
                "val": 1,
                "group": 1
            },
            {
                "id": "potential clinical utility of imaging technique in differential diagnosis",
                "name": "potential clinical utility of imaging technique in differential diagnosis",
                "val": 1,
                "group": 1
            },
            {
                "id": "clinical,imaging technique",
                "name": "clinical,imaging technique",
                "val": 5,
                "group": 1
            },
            {
                "id": "clinical,imaging technique,differential diagnosis",
                "name": "clinical,imaging technique,differential diagnosis",
                "val": 1,
                "group": 1
            },
            {
                "id": "potential utility of imaging technique in differential diagnosis",
                "name": "potential utility of imaging technique in differential diagnosis",
                "val": 2,
                "group": 1
            },
            {
                "id": "imaging technique,differential diagnosis",
                "name": "imaging technique,differential diagnosis",
                "val": 1,
                "group": 1
            },
            {
                "id": "potential utility of imaging technique",
                "name": "potential utility of imaging technique",
                "val": 2,
                "group": 1
            },
            {
                "id": "potential clinical utility of imaging technique in diagnosis",
                "name": "potential clinical utility of imaging technique in diagnosis",
                "val": 1,
                "group": 1
            },
            {
                "id": "potential clinical utility in diagnosis",
                "name": "potential clinical utility in diagnosis",
                "val": 1,
                "group": 1
            },
            {
                "id": "potential utility in differential diagnosis",
                "name": "potential utility in differential diagnosis",
                "val": 3,
                "group": 1
            },
            {
                "id": "potential clinical utility of imaging technique",
                "name": "potential clinical utility of imaging technique",
                "val": 1,
                "group": 1
            },
            {
                "id": "potential clinical utility",
                "name": "potential clinical utility",
                "val": 1,
                "group": 1
            },
            {
                "id": "potential utility",
                "name": "potential utility",
                "val": 4,
                "group": 1
            },
            {"id": "Keywords", "name": "Keywords", "val": 7, "group": 1},
            {"id": "19", "name": "19", "val": 10, "group": 1},
            {"id": "novel", "name": "novel", "val": 2, "group": 1},
            {"id": "article", "name": "article", "val": 10, "group": 1},
            {"id": "rapid", "name": "rapid", "val": 2, "group": 1},
            {"id": "assessed", "name": "assessed", "val": 4, "group": 1},
            {
                "id": "Topical Collection",
                "name": "Topical Collection",
                "val": 3,
                "group": 1
            },
            {
                "id": "Topical Collection,Infection",
                "name": "Topical Collection,Infection",
                "val": 1,
                "group": 1
            },
            {
                "id": "Nuclear Medicine",
                "name": "Nuclear Medicine",
                "val": 1,
                "group": 1
            },
            {"id": "Tongji Medical", "name": "Tongji Medical", "val": 1, "group": 1},
            {"id": "College", "name": "College", "val": 3, "group": 1},
            {"id": "Science", "name": "Science", "val": 3, "group": 1},
            {"id": "December 2019", "name": "December 2019", "val": 3, "group": 1},
            {"id": "cough", "name": "cough", "val": 4, "group": 1},
            {"id": "breath", "name": "breath", "val": 4, "group": 1},
            {"id": "detection", "name": "detection", "val": 3, "group": 1},
            {"id": "gold standard", "name": "gold standard", "val": 3, "group": 1},
            {"id": "reasons", "name": "reasons", "val": 10, "group": 1},
            {"id": "lack", "name": "lack", "val": 4, "group": 1},
            {
                "id": "lack of standard operation",
                "name": "lack of standard operation",
                "val": 1,
                "group": 1
            },
            {
                "id": "lack of operation",
                "name": "lack of operation",
                "val": 1,
                "group": 1
            },
            {"id": "based", "name": "based", "val": 3, "group": 1},
            {
                "id": "exposure history clinical",
                "name": "exposure history clinical",
                "val": 2,
                "group": 1
            },
            {
                "id": "exposure history",
                "name": "exposure history",
                "val": 8,
                "group": 1
            },
            {
                "id": "exposure history,clinical",
                "name": "exposure history,clinical",
                "val": 2,
                "group": 1
            },
            {
                "id": "generally based",
                "name": "generally based",
                "val": 3,
                "group": 1
            },
            {"id": "consolidations", "name": "consolidations", "val": 3, "group": 1},
            {"id": "multiple", "name": "multiple", "val": 5, "group": 1},
            {
                "id": "multiple,lobular",
                "name": "multiple,lobular",
                "val": 2,
                "group": 1
            },
            {"id": "tients", "name": "tients", "val": 2, "group": 1},
            {"id": "addition", "name": "addition", "val": 2, "group": 1},
            {"id": "we", "name": "we", "val": 6, "group": 1},
            {"id": "FDG", "name": "FDG", "val": 6, "group": 1},
            {"id": "Union Hospital", "name": "Union Hospital", "val": 5, "group": 1},
            {"id": "lung GGOs", "name": "lung GGOs", "val": 1, "group": 1},
            {"id": "lung", "name": "lung", "val": 3, "group": 1},
            {"id": "lung,GGOs", "name": "lung,GGOs", "val": 3, "group": 1},
            {"id": "throat", "name": "throat", "val": 1, "group": 1},
            {"id": "days", "name": "days", "val": 2, "group": 1},
            {"id": "sore throat", "name": "sore throat", "val": 3, "group": 1},
            {"id": "3 days", "name": "3 days", "val": 2, "group": 1},
            {"id": "testing", "name": "testing", "val": 7, "group": 1},
            {"id": "the", "name": "the", "val": 6, "group": 1},
            {"id": "WBC count", "name": "WBC count", "val": 2, "group": 1},
            {"id": "IgM", "name": "IgM", "val": 20, "group": 1},
            {"id": "results", "name": "results", "val": 10, "group": 1},
            {
                "id": "negative results",
                "name": "negative results",
                "val": 2,
                "group": 1
            },
            {"id": "negative", "name": "negative", "val": 5, "group": 1},
            {
                "id": "negative,results",
                "name": "negative,results",
                "val": 6,
                "group": 1
            },
            {"id": "18F FDG PET CT", "name": "18F FDG PET CT", "val": 3, "group": 1},
            {
                "id": "peripheral,GGOs",
                "name": "peripheral",
                "val": 3,
                "group": 1,
                "articles": [
                    "test",
                    "test2"
                ]
            },
            {"id": "GGOs", "name": "GGOs", "val": 20, "group": 1},
            {"id": "increased", "name": "increased", "val": 7, "group": 1},
            {
                "id": "increased,uptake",
                "name": "increased,uptake",
                "val": 6,
                "group": 1
            },
            {"id": "performed", "name": "performed", "val": 3, "group": 1},
            {"id": "man", "name": "man", "val": 2, "group": 1},
            {
                "id": "recent history of surgery",
                "name": "recent history of surgery",
                "val": 1,
                "group": 1
            },
            {
                "id": "history of surgery",
                "name": "history of surgery",
                "val": 1,
                "group": 1
            },
            {"id": "event", "name": "event", "val": 4, "group": 1},
            {"id": "hospital", "name": "hospital", "val": 5, "group": 1},
            {"id": "history", "name": "history", "val": 7, "group": 1},
            {"id": "matic event", "name": "matic event", "val": 9, "group": 1},
            {
                "id": "8 day history of",
                "name": "8 day history of",
                "val": 2,
                "group": 1
            },
            {"id": "8 day history", "name": "8 day history", "val": 3, "group": 1},
            {"id": "ing", "name": "ing", "val": 2, "group": 1},
            {"id": "fatigue", "name": "fatigue", "val": 5, "group": 1},
            {"id": "afternoon", "name": "afternoon", "val": 3, "group": 1},
            {"id": "Cough", "name": "Cough", "val": 4, "group": 1},
            {"id": "erence range", "name": "erence range", "val": 1, "group": 1},
            {"id": "neutrophils", "name": "neutrophils", "val": 1, "group": 1},
            {"id": "January", "name": "January", "val": 24, "group": 1},
            {
                "id": "FDG positive GGOs",
                "name": "FDG positive GGOs",
                "val": 2,
                "group": 1
            },
            {"id": "multiple GGOs", "name": "multiple GGOs", "val": 2, "group": 1},
            {
                "id": "multiple FDG positive GGOs",
                "name": "multiple FDG positive GGOs",
                "val": 2,
                "group": 1
            },
            {
                "id": "consolidative opacities",
                "name": "consolidative opacities",
                "val": 3,
                "group": 1
            },
            {"id": "lungs", "name": "lungs", "val": 18, "group": 1},
            {"id": "cases", "name": "cases", "val": 11, "group": 1},
            {"id": "GGO", "name": "GGO", "val": 2, "group": 1},
            {
                "id": "interlobular septal",
                "name": "interlobular septal",
                "val": 2,
                "group": 1
            },
            {"id": "pathogens", "name": "pathogens", "val": 13, "group": 1},
            {"id": "investigated", "name": "investigated", "val": 22, "group": 1},
            {
                "id": "following pathogens",
                "name": "following pathogens",
                "val": 5,
                "group": 1
            },
            {
                "id": "respiratory pathogens",
                "name": "respiratory pathogens",
                "val": 12,
                "group": 1
            },
            {
                "id": "right upper lung",
                "name": "right upper lung",
                "val": 5,
                "group": 1
            },
            {"id": "Peripheral", "name": "Peripheral", "val": 7, "group": 1},
            {
                "id": "increased 18F FDG uptake in right upper lung",
                "name": "increased 18F FDG uptake in right upper lung",
                "val": 2,
                "group": 1
            },
            {
                "id": "Peripheral,GGOs",
                "name": "Peripheral,GGOs",
                "val": 27,
                "group": 1,
                "articles": [
                    "COVID Research - Shrek University",
                    "How does COVID affect Ogres - Prof. Shrek",
                    "adfasdfasdf",
                    "adsfasdf",
                    "asdfa"
                ]
            },
            {
                "id": "increased,uptake,right upper lung",
                "name": "increased,uptake,right upper lung",
                "val": 2,
                "group": 1
            },
            {"id": "lymph nodes", "name": "lymph nodes", "val": 7, "group": 1},
            {"id": "mediastinum", "name": "mediastinum", "val": 20, "group": 1},
            {"id": "smaller", "name": "smaller", "val": 2, "group": 1},
            {"id": "shadow", "name": "shadow", "val": 5, "group": 1},
            {
                "id": "right upper lung lobe",
                "name": "right upper lung lobe",
                "val": 2,
                "group": 1
            },
            {"id": "solid nodule", "name": "solid nodule", "val": 3, "group": 1},
            {
                "id": "left lower lung lobe",
                "name": "left lower lung lobe",
                "val": 1,
                "group": 1
            },
            {"id": "left lower", "name": "left lower", "val": 1, "group": 1},
            {
                "id": "left lower,lung lobe",
                "name": "left lower,lung lobe",
                "val": 1,
                "group": 1
            },
            {"id": "right lung", "name": "right lung", "val": 12, "group": 1},
            {"id": "ment", "name": "ment", "val": 6, "group": 1},
            {"id": "symp", "name": "symp", "val": 3, "group": 1},
            {
                "id": "antiviral drugs",
                "name": "antiviral drugs",
                "val": 1,
                "group": 1
            },
            {"id": "antiviral", "name": "antiviral", "val": 4, "group": 1},
            {
                "id": "negative findings",
                "name": "negative findings",
                "val": 1,
                "group": 1
            },
            {
                "id": "negative,findings",
                "name": "negative,findings",
                "val": 4,
                "group": 1
            },
            {"id": "findings", "name": "findings", "val": 14, "group": 1},
            {"id": "identification", "name": "identification", "val": 8, "group": 1},
            {
                "id": "identification of blurry",
                "name": "identification of blurry",
                "val": 2,
                "group": 1
            },
            {
                "id": "identification,blurry",
                "name": "identification,blurry",
                "val": 2,
                "group": 1
            },
            {
                "id": "right lower lung lobe",
                "name": "right lower lung lobe",
                "val": 1,
                "group": 1
            },
            {"id": "right lower", "name": "right lower", "val": 1, "group": 1},
            {
                "id": "right lower,lung lobe",
                "name": "right lower,lung lobe",
                "val": 1,
                "group": 1
            },
            {"id": "thicken", "name": "thicken", "val": 4, "group": 1},
            {
                "id": "SARS CoV 2 nucleic acid",
                "name": "SARS CoV 2 nucleic acid",
                "val": 3,
                "group": 1
            },
            {
                "id": "SARS CoV nucleic acid",
                "name": "SARS CoV nucleic acid",
                "val": 3,
                "group": 1
            },
            {"id": "1 2020", "name": "1 2020", "val": 2, "group": 1},
            {"id": "significant", "name": "significant", "val": 1, "group": 1},
            {"id": "picture", "name": "picture", "val": 3, "group": 1},
            {
                "id": "significant,improvement",
                "name": "significant,improvement",
                "val": 2,
                "group": 1
            },
            {"id": "Hospital", "name": "Hospital", "val": 6, "group": 1},
            {
                "id": "8 day history of fever",
                "name": "8 day history of fever",
                "val": 1,
                "group": 1
            },
            {"id": "history,fever", "name": "history,fever", "val": 1, "group": 1},
            {"id": "interpersonal", "name": "interpersonal", "val": 2, "group": 1},
            {"id": "COVID", "name": "COVID", "val": 1, "group": 1},
            {"id": "travel", "name": "travel", "val": 2, "group": 1},
            {"id": "exposure", "name": "exposure", "val": 4, "group": 1},
            {"id": "travel,history", "name": "travel,history", "val": 6, "group": 1},
            {"id": "exposure known", "name": "exposure known", "val": 4, "group": 1},
            {"id": "consistent", "name": "consistent", "val": 4, "group": 1},
            {"id": "report", "name": "report", "val": 6, "group": 1},
            {"id": "current report", "name": "current report", "val": 2, "group": 1},
            {
                "id": "presence of peripheral",
                "name": "presence of peripheral",
                "val": 1,
                "group": 1
            },
            {"id": "presence", "name": "presence", "val": 4, "group": 1},
            {
                "id": "presence,peripheral",
                "name": "presence,peripheral",
                "val": 1,
                "group": 1
            },
            {"id": "more two pulmo", "name": "more two pulmo", "val": 2, "group": 1},
            {"id": "parenchyma", "name": "parenchyma", "val": 3, "group": 1},
            {"id": "can observed", "name": "can observed", "val": 3, "group": 1},
            {"id": "unlikely", "name": "unlikely", "val": 1, "group": 1},
            {"id": "as unlikely", "name": "as unlikely", "val": 1, "group": 1},
            {
                "id": "pulmonary infections",
                "name": "pulmonary infections",
                "val": 4,
                "group": 1
            },
            {"id": "inflam", "name": "inflam", "val": 2, "group": 1},
            {
                "id": "significant inflam",
                "name": "significant inflam",
                "val": 2,
                "group": 1
            },
            {
                "id": "lymphadenopathy",
                "name": "lymphadenopathy",
                "val": 2,
                "group": 1
            },
            {
                "id": "our 18F FDG PET",
                "name": "our 18F FDG PET",
                "val": 2,
                "group": 1
            },
            {"id": "CT", "name": "CT", "val": 3, "group": 1},
            {"id": "three", "name": "three", "val": 6, "group": 1},
            {"id": "CT,findings", "name": "CT,findings", "val": 15, "group": 1},
            {
                "id": "increased nodal FDG uptake",
                "name": "increased nodal FDG uptake",
                "val": 2,
                "group": 1
            },
            {
                "id": "increased,nodal",
                "name": "increased,nodal",
                "val": 1,
                "group": 1
            },
            {
                "id": "increased,nodal,FDG",
                "name": "increased,nodal,FDG",
                "val": 1,
                "group": 1
            },
            {
                "id": "increased,nodal,FDG,uptake",
                "name": "increased,nodal,FDG,uptake",
                "val": 1,
                "group": 1
            },
            {
                "id": "nodal FDG uptake",
                "name": "nodal FDG uptake",
                "val": 3,
                "group": 1
            },
            {"id": "nodal", "name": "nodal", "val": 1, "group": 1},
            {"id": "nodal,FDG", "name": "nodal,FDG", "val": 1, "group": 1},
            {
                "id": "nodal,FDG,uptake",
                "name": "nodal,FDG,uptake",
                "val": 1,
                "group": 1
            },
            {"id": "first time", "name": "first time", "val": 6, "group": 1},
            {"id": "imaging,data", "name": "imaging,data", "val": 4, "group": 1},
            {"id": "time", "name": "time", "val": 6, "group": 1},
            {"id": "Multiple", "name": "Multiple", "val": 1, "group": 1},
            {
                "id": "Multiple,peripheral",
                "name": "Multiple,peripheral",
                "val": 2,
                "group": 1
            },
            {
                "id": "Multiple,peripheral,GGOs",
                "name": "Multiple,peripheral,GGOs",
                "val": 6,
                "group": 1
            },
            {
                "id": "interlobular septal thickening",
                "name": "interlobular septal thickening",
                "val": 9,
                "group": 1
            },
            {"id": "data", "name": "data", "val": 18, "group": 1},
            {
                "id": "primates exposed to MERS",
                "name": "primates exposed to MERS",
                "val": 3,
                "group": 1
            },
            {
                "id": "non-human primates exposed to MERS",
                "name": "non-human primates exposed to MERS",
                "val": 1,
                "group": 1
            },
            {
                "id": "non-human primates",
                "name": "non-human primates",
                "val": 7,
                "group": 1
            },
            {
                "id": "non-human primates exposed",
                "name": "non-human primates exposed",
                "val": 1,
                "group": 1
            },
            {
                "id": "primates exposed",
                "name": "primates exposed",
                "val": 3,
                "group": 1
            },
            {"id": "primates", "name": "primates", "val": 3, "group": 1},
            {"id": "evident", "name": "evident", "val": 3, "group": 1},
            {"id": "our patients", "name": "our patients", "val": 3, "group": 1},
            {
                "id": "fectious diseases",
                "name": "fectious diseases",
                "val": 2,
                "group": 1
            },
            {"id": "this", "name": "this", "val": 2, "group": 1},
            {
                "id": "complementary diagnostic role",
                "name": "complementary diagnostic role",
                "val": 2,
                "group": 1
            },
            {
                "id": "imaging,modality",
                "name": "imaging,modality",
                "val": 8,
                "group": 1
            },
            {
                "id": "diagnostic role",
                "name": "diagnostic role",
                "val": 4,
                "group": 1
            },
            {
                "id": "complementary role",
                "name": "complementary role",
                "val": 3,
                "group": 1
            },
            {"id": "role", "name": "role", "val": 3, "group": 1},
            {"id": "case series", "name": "case series", "val": 4, "group": 1},
            {
                "id": "small sample size",
                "name": "small sample size",
                "val": 1,
                "group": 1
            },
            {"id": "sample size", "name": "sample size", "val": 3, "group": 1},
            {
                "id": "may explained by several reasons including 1",
                "name": "may explained by several reasons including 1",
                "val": 1,
                "group": 1
            },
            {
                "id": "may explained by reasons",
                "name": "may explained by reasons",
                "val": 1,
                "group": 1
            },
            {
                "id": "may explained by reasons including 1",
                "name": "may explained by reasons including 1",
                "val": 1,
                "group": 1
            },
            {
                "id": "may explained by several reasons",
                "name": "may explained by several reasons",
                "val": 1,
                "group": 1
            },
            {"id": "differences", "name": "differences", "val": 3, "group": 1},
            {"id": "sample", "name": "sample", "val": 3, "group": 1},
            {"id": "caveats", "name": "caveats", "val": 4, "group": 1},
            {
                "id": "COVID 19 pneumonia",
                "name": "COVID 19 pneumonia",
                "val": 2,
                "group": 1
            },
            {"id": "Compliance", "name": "Compliance", "val": 2, "group": 1},
            {
                "id": "ethical standards",
                "name": "ethical standards",
                "val": 2,
                "group": 1
            },
            {"id": "tive study", "name": "tive study", "val": 4, "group": 1},
            {"id": "insti", "name": "insti", "val": 4, "group": 1},
            {"id": "consent", "name": "consent", "val": 2, "group": 1},
            {"id": "waived", "name": "waived", "val": 2, "group": 1}
        ],
        "links": [
            {"source": "findings", "target": "reasons", "label": "may"},
            {
                "source": "findings",
                "target": "may explained by several reasons including 1",
                "label": "may"
            },
            {
                "source": "findings",
                "target": "may explained by reasons",
                "label": "may"
            },
            {
                "source": "findings",
                "target": "may explained by reasons including 1",
                "label": "may"
            },
            {
                "source": "findings",
                "target": "may explained by several reasons",
                "label": "may"
            },
            {"source": "cases", "target": "China", "label": "is in"},
            {"source": "cases", "target": "COVID 19", "label": "is with"},
            {
                "source": "cases",
                "target": "presence",
                "label": "were characterized by"
            },
            {
                "source": "cases",
                "target": "presence of peripheral",
                "label": "were characterized by"
            },
            {
                "source": "cases",
                "target": "presence,peripheral",
                "label": "were characterized by"
            },
            {"source": "Germany", "target": "Springer Nature", "label": "part of"},
            {"source": "Germany,Springer", "target": "Springer", "label": "part of"},
            {
                "source": "case series",
                "target": "sample size",
                "label": "is limited by"
            },
            {
                "source": "case series",
                "target": "small sample size",
                "label": "is limited by"
            },
            {"source": "patients", "target": "consistent", "label": "are"},
            {"source": "patients", "target": "report", "label": "described in"},
            {
                "source": "patients",
                "target": "current report",
                "label": "described in"
            },
            {"source": "patients", "target": "peripheral", "label": "had"},
            {
                "source": "patients",
                "target": "ground glass opacities",
                "label": "had"
            },
            {
                "source": "patients",
                "target": "peripheral ground glass opacities",
                "label": "had"
            },
            {
                "source": "patients",
                "target": "acute respiratory disease",
                "label": "is with"
            },
            {
                "source": "patients",
                "target": "COVID 19 pneumonia",
                "label": "is with"
            },
            {"source": "aim", "target": "patients", "label": "is illustrate"},
            {
                "source": "aim",
                "target": "patients,acute respiratory disease",
                "label": "is illustrate"
            },
            {"source": "COVID 19", "target": "pulmonary", "label": "has"},
            {"source": "COVID 19", "target": "tropism", "label": "has"},
            {"source": "COVID 19", "target": "pulmonary,tropism", "label": "has"},
            {"source": "COVID 19", "target": "lung", "label": "have"},
            {"source": "COVID 19", "target": "interpersonal", "label": "have"},
            {"source": "COVID 19", "target": "Wuhan", "label": "is in"},
            {"source": "COVID 19", "target": "China", "label": "province of"},
            {
                "source": "Methods",
                "target": "18F FDG PET CT results",
                "label": "describe"
            },
            {
                "source": "Methods",
                "target": "patients",
                "label": "describe 18F FDG PET CT results from"
            },
            {
                "source": "Methods",
                "target": "four patients",
                "label": "describe 18F FDG PET CT results from"
            },
            {
                "source": "We",
                "target": "patients",
                "label": "describe 18F FDG PET CT results from"
            },
            {"source": "January", "target": "identification", "label": "led to"},
            {
                "source": "January",
                "target": "identification of blurry",
                "label": "led to"
            },
            {
                "source": "January",
                "target": "identification,blurry",
                "label": "led to"
            },
            {"source": "January", "target": "GGOs", "label": "revealed"},
            {"source": "January", "target": "FDG positive GGOs", "label": "revealed"},
            {"source": "January", "target": "multiple GGOs", "label": "revealed"},
            {
                "source": "January",
                "target": "multiple FDG positive GGOs",
                "label": "revealed"
            },
            {"source": "outbreak", "target": "novel", "label": "caused by"},
            {"source": "outbreak", "target": "still unrecognized", "label": "was"},
            {
                "source": "outbreak",
                "target": "when still unrecognized",
                "label": "was"
            },
            {"source": "outbreak", "target": "unrecognized", "label": "was"},
            {"source": "outbreak", "target": "when unrecognized", "label": "was"},
            {"source": "virus", "target": "unknown", "label": "was"},
            {
                "source": "clinical",
                "target": "differential diagnosis",
                "label": "is in"
            },
            {"source": "virus,infectivity", "target": "unknown", "label": "was"},
            {
                "source": "imaging",
                "target": "first time",
                "label": "evident indicate for"
            },
            {"source": "imaging", "target": "time",
                "label": "evident indicate for"},
            {"source": "imaging", "target": "first time", "label": "indicate for"},
            {"source": "imaging", "target": "time", "label": "indicate for"},
            {"source": "imaging", "target": "diagnostic role", "label": "may play"},
            {
                "source": "imaging",
                "target": "complementary diagnostic role",
                "label": "may play"
            },
            {
                "source": "imaging",
                "target": "complementary role",
                "label": "may play"
            },
            {"source": "imaging", "target": "role", "label": "may play"},
            {
                "source": "imaging",
                "target": "diagnosis",
                "label": "strongly suggested"
            },
            {
                "source": "imaging",
                "target": "diagnosis of COVID 19",
                "label": "strongly suggested"
            },
            {"source": "imaging", "target": "diagnosis", "label": "suggested"},
            {
                "source": "imaging",
                "target": "diagnosis of COVID 19",
                "label": "suggested"
            },
            {"source": "diagnosis", "target": "based", "label": "is"},
            {"source": "diagnosis", "target": "generally based", "label": "is"},
            {
                "source": "diagnosis",
                "target": "exposure history",
                "label": "is based on"
            },
            {
                "source": "diagnosis",
                "target": "exposure history clinical",
                "label": "is based on"
            },
            {
                "source": "diagnosis",
                "target": "exposure history,clinical",
                "label": "is based on"
            },
            {
                "source": "diagnosis",
                "target": "exposure history",
                "label": "is generally based on"
            },
            {
                "source": "diagnosis",
                "target": "exposure history clinical",
                "label": "is generally based on"
            },
            {
                "source": "diagnosis",
                "target": "exposure history,clinical",
                "label": "is generally based on"
            },
            {
                "source": "imaging,findings",
                "target": "diagnosis",
                "label": "strongly suggested"
            },
            {
                "source": "imaging,findings",
                "target": "diagnosis of COVID 19",
                "label": "strongly suggested"
            },
            {
                "source": "imaging,findings",
                "target": "diagnosis",
                "label": "suggested"
            },
            {
                "source": "imaging,findings",
                "target": "diagnosis of COVID 19",
                "label": "suggested"
            },
            {"source": "peripheral", "target": "thicken", "label": "is with"},
            {"source": "lesions", "target": "smaller", "label": "were"},
            {"source": "lesions", "target": "evident", "label": "were"},
            {
                "source": "lesions",
                "target": "uptake",
                "label": "were characterized by"
            },
            {
                "source": "lesions",
                "target": "18F FDG uptake",
                "label": "were characterized by"
            },
            {
                "source": "lesions",
                "target": "high 18F FDG uptake",
                "label": "were characterized by"
            },
            {
                "source": "lesions",
                "target": "our patients",
                "label": "were evident in"
            },
            {"source": "inated disease", "target": "absent", "label": "was"},
            {"source": "disease", "target": "absent", "label": "was"},
            {"source": "pilot data", "target": "light", "label": "shed"},
            {"source": "pilot data", "target": "clinical", "label": "shed light on"},
            {
                "source": "pilot data",
                "target": "imaging technique",
                "label": "shed light on"
            },
            {
                "source": "pilot data",
                "target": "differential diagnosis",
                "label": "shed light on"
            },
            {
                "source": "pilot data",
                "target": "potential utility of imaging technique in diagnosis",
                "label": "shed light on"
            },
            {
                "source": "pilot data",
                "target": "potential utility in diagnosis",
                "label": "shed light on"
            },
            {
                "source": "pilot data",
                "target": "potential clinical utility in differential diagnosis",
                "label": "shed light on"
            },
            {
                "source": "pilot data",
                "target": "clinical,differential diagnosis",
                "label": "shed light on"
            },
            {
                "source": "pilot data",
                "target": "potential clinical utility of imaging technique in differential diagnosis",
                "label": "shed light on"
            },
            {
                "source": "pilot data",
                "target": "clinical,imaging technique",
                "label": "shed light on"
            },
            {
                "source": "pilot data",
                "target": "clinical,imaging technique,differential diagnosis",
                "label": "shed light on"
            },
            {
                "source": "pilot data",
                "target": "potential utility of imaging technique in differential diagnosis",
                "label": "shed light on"
            },
            {
                "source": "pilot data",
                "target": "imaging technique,differential diagnosis",
                "label": "shed light on"
            },
            {
                "source": "pilot data",
                "target": "potential utility of imaging technique",
                "label": "shed light on"
            },
            {
                "source": "pilot data",
                "target": "potential clinical utility of imaging technique in diagnosis",
                "label": "shed light on"
            },
            {
                "source": "pilot data",
                "target": "potential clinical utility in diagnosis",
                "label": "shed light on"
            },
            {
                "source": "pilot data",
                "target": "potential utility in differential diagnosis",
                "label": "shed light on"
            },
            {
                "source": "pilot data",
                "target": "potential clinical utility of imaging technique",
                "label": "shed light on"
            },
            {
                "source": "pilot data",
                "target": "potential clinical utility",
                "label": "shed light on"
            },
            {
                "source": "pilot data",
                "target": "potential utility",
                "label": "shed light on"
            },
            {"source": "Keywords", "target": "19", "label": "COVID"},
            {"source": "19", "target": "pulmonary", "label": "has"},
            {"source": "19", "target": "tropism", "label": "has"},
            {"source": "19", "target": "pulmonary,tropism", "label": "has"},
            {"source": "article", "target": "rapid", "label": "ensure"},
            {"source": "article", "target": "assessed", "label": "has"},
            {
                "source": "article",
                "target": "Topical Collection",
                "label": "is part of"
            },
            {
                "source": "article",
                "target": "Topical Collection,Infection",
                "label": "is part of"
            },
            {"source": "Union Hospital", "target": "lung", "label": "is with"},
            {"source": "Union Hospital", "target": "lung GGOs", "label": "is with"},
            {"source": "Union Hospital", "target": "lung,GGOs", "label": "is with"},
            {
                "source": "Nuclear Medicine",
                "target": "Tongji Medical",
                "label": "of Department is"
            },
            {"source": "College", "target": "Science", "label": "University of"},
            {"source": "December 2019", "target": "Wuhan", "label": "is in"},
            {"source": "cough", "target": "breath", "label": "shortness of"},
            {"source": "detection", "target": "gold standard", "label": "remains"},
            {"source": "reasons", "target": "lack", "label": "may include"},
            {
                "source": "reasons",
                "target": "lack of standard operation",
                "label": "may include"
            },
            {
                "source": "reasons",
                "target": "lack of operation",
                "label": "may include"
            },
            {"source": "GGOs", "target": "unlikely", "label": "are"},
            {"source": "GGOs", "target": "as unlikely", "label": "are"},
            {"source": "GGOs", "target": "right lung", "label": "is in"},
            {"source": "GGOs", "target": "lungs", "label": "is in"},
            {"source": "GGOs", "target": "more two pulmo", "label": "is in"},
            {"source": "multiple", "target": "mediastinum", "label": "is in"},
            {"source": "consolidations", "target": "multiple", "label": "is in"},
            {
                "source": "consolidations",
                "target": "multiple,lobular",
                "label": "is in"
            },
            {"source": "tients", "target": "addition", "label": "should prompt"},
            {"source": "we", "target": "FDG", "label": "Here report"},
            {"source": "we", "target": "FDG", "label": "report"},
            {"source": "man", "target": "history of surgery", "label": "is with"},
            {
                "source": "man",
                "target": "recent history of surgery",
                "label": "is with"
            },
            {"source": "sore throat", "target": "days", "label": "lasting for"},
            {"source": "sore throat", "target": "3 days", "label": "lasting for"},
            {"source": "throat", "target": "days", "label": "lasting for"},
            {"source": "testing", "target": "WBC count", "label": "revealed"},
            {
                "source": "testing",
                "target": "the",
                "label": "revealed WBC count within"
            },
            {"source": "testing", "target": "performed", "label": "was"},
            {
                "source": "respiratory pathogens",
                "target": "investigated",
                "label": "were"
            },
            {"source": "IgM", "target": "results", "label": "yielded"},
            {"source": "IgM", "target": "negative", "label": "yielded"},
            {"source": "IgM", "target": "negative results", "label": "yielded"},
            {"source": "IgM", "target": "negative,results", "label": "yielded"},
            {"source": "GGO", "target": "interlobular septal", "label": "is with"},
            {
                "source": "18F FDG PET CT",
                "target": "peripheral",
                "label": "identified"
            },
            {"source": "18F FDG PET CT", "target": "GGOs", "label": "identified"},
            {
                "source": "18F FDG PET CT",
                "target": "peripheral,GGOs",
                "label": "identified"
            },
            {"source": "peripheral,GGOs", "target": "thicken", "label": "is with"},
            {"source": "increased", "target": "the", "label": "is in"},
            {"source": "increased", "target": "right upper lung", "label": "is in"},
            {"source": "increased,uptake", "target": "the", "label": "is in"},
            {
                "source": "increased,uptake",
                "target": "right upper lung",
                "label": "is in"
            },
            {"source": "matic event", "target": "hospital", "label": "presented to"},
            {"source": "matic event", "target": "history", "label": "presented with"},
            {
                "source": "matic event",
                "target": "8 day history of",
                "label": "presented with"
            },
            {
                "source": "matic event",
                "target": "8 day history",
                "label": "presented with"
            },
            {"source": "event", "target": "hospital", "label": "presented to"},
            {"source": "event", "target": "history", "label": "presented with"},
            {"source": "afternoon", "target": "fatigue", "label": "accompanied by"},
            {"source": "ing", "target": "fatigue", "label": "accompanied by"},
            {"source": "Cough", "target": "absent", "label": "were"},
            {"source": "erence range", "target": "neutrophils", "label": "is with"},
            {"source": "pathogens", "target": "investigated", "label": "were"},
            {"source": "pathogens", "target": "findings", "label": "yielded"},
            {"source": "pathogens", "target": "negative", "label": "yielded"},
            {
                "source": "pathogens",
                "target": "negative findings",
                "label": "yielded"
            },
            {
                "source": "pathogens",
                "target": "negative,findings",
                "label": "yielded"
            },
            {
                "source": "consolidative opacities",
                "target": "lungs",
                "label": "is in"
            },
            {
                "source": "following pathogens",
                "target": "investigated",
                "label": "were"
            },
            {"source": "Peripheral", "target": "lungs", "label": "is in"},
            {"source": "Peripheral", "target": "mediastinum", "label": "is in"},
            {
                "source": "Peripheral",
                "target": "increased 18F FDG uptake in right upper lung",
                "label": "is with"
            },
            {
                "source": "Peripheral",
                "target": "interlobular septal thickening",
                "label": "is with"
            },
            {"source": "Peripheral,GGOs", "target": "lungs", "label": "is in"},
            {"source": "Peripheral,GGOs", "target": "mediastinum", "label": "is in"},
            {"source": "Peripheral,GGOs", "target": "increased", "label": "is with"},
            {
                "source": "Peripheral,GGOs",
                "target": "increased,uptake",
                "label": "is with"
            },
            {
                "source": "Peripheral,GGOs",
                "target": "increased 18F FDG uptake in right upper lung",
                "label": "is with"
            },
            {
                "source": "Peripheral,GGOs",
                "target": "increased,uptake,right upper lung",
                "label": "is with"
            },
            {
                "source": "Peripheral,GGOs",
                "target": "interlobular septal thickening",
                "label": "is with"
            },
            {"source": "lymph nodes", "target": "mediastinum", "label": "is in"},
            {"source": "shadow", "target": "right lower", "label": "is in"},
            {"source": "shadow", "target": "right upper lung lobe", "label": "is in"},
            {"source": "shadow", "target": "right lower lung lobe", "label": "is in"},
            {"source": "shadow", "target": "right lower,lung lobe", "label": "is in"},
            {"source": "solid nodule", "target": "left lower", "label": "is in"},
            {
                "source": "solid nodule",
                "target": "left lower lung lobe",
                "label": "is in"
            },
            {
                "source": "solid nodule",
                "target": "left lower,lung lobe",
                "label": "is in"
            },
            {"source": "Multiple", "target": "right lung", "label": "is in"},
            {"source": "ment", "target": "antiviral", "label": "is with"},
            {"source": "ment", "target": "antiviral drugs", "label": "is with"},
            {"source": "ment", "target": "symp", "label": "led to"},
            {
                "source": "SARS CoV 2 nucleic acid",
                "target": "findings",
                "label": "yielded"
            },
            {
                "source": "SARS CoV 2 nucleic acid",
                "target": "negative",
                "label": "yielded"
            },
            {
                "source": "SARS CoV 2 nucleic acid",
                "target": "negative,findings",
                "label": "yielded"
            },
            {
                "source": "SARS CoV nucleic acid",
                "target": "findings",
                "label": "yielded"
            },
            {
                "source": "SARS CoV nucleic acid",
                "target": "negative",
                "label": "yielded"
            },
            {
                "source": "SARS CoV nucleic acid",
                "target": "negative,findings",
                "label": "yielded"
            },
            {"source": "1 2020", "target": "antiviral", "label": "performed after"},
            {"source": "significant", "target": "picture", "label": "is in"},
            {
                "source": "significant,improvement",
                "target": "picture",
                "label": "is in"
            },
            {"source": "Hospital", "target": "history", "label": "presented with"},
            {
                "source": "Hospital",
                "target": "8 day history",
                "label": "presented with"
            },
            {
                "source": "Hospital",
                "target": "8 day history of fever",
                "label": "presented with"
            },
            {
                "source": "Hospital",
                "target": "history,fever",
                "label": "presented with"
            },
            {"source": "COVID", "target": "interpersonal", "label": "have"},
            {"source": "travel", "target": "exposure", "label": "coupled with"},
            {"source": "travel", "target": "exposure known", "label": "coupled with"},
            {
                "source": "travel,history",
                "target": "exposure",
                "label": "coupled with"
            },
            {
                "source": "travel,history",
                "target": "exposure known",
                "label": "coupled with"
            },
            {"source": "parenchyma", "target": "can observed", "label": "can"},
            {
                "source": "pulmonary infections",
                "target": "inflam",
                "label": "reflects"
            },
            {
                "source": "pulmonary infections",
                "target": "significant inflam",
                "label": "reflects"
            },
            {
                "source": "lymphadenopathy",
                "target": "our 18F FDG PET",
                "label": "by accompanied is"
            },
            {
                "source": "CT",
                "target": "increased nodal FDG uptake",
                "label": "revealed"
            },
            {"source": "CT", "target": "nodal FDG uptake", "label": "revealed"},
            {
                "source": "CT",
                "target": "three",
                "label": "revealed nodal FDG uptake in"
            },
            {"source": "CT,findings", "target": "increased", "label": "revealed"},
            {"source": "CT,findings", "target": "nodal", "label": "revealed"},
            {
                "source": "CT,findings",
                "target": "increased nodal FDG uptake",
                "label": "revealed"
            },
            {
                "source": "CT,findings",
                "target": "increased,nodal",
                "label": "revealed"
            },
            {
                "source": "CT,findings",
                "target": "increased,nodal,FDG",
                "label": "revealed"
            },
            {
                "source": "CT,findings",
                "target": "increased,nodal,FDG,uptake",
                "label": "revealed"
            },
            {
                "source": "CT,findings",
                "target": "nodal FDG uptake",
                "label": "revealed"
            },
            {"source": "CT,findings", "target": "nodal,FDG", "label": "revealed"},
            {
                "source": "CT,findings",
                "target": "nodal,FDG,uptake",
                "label": "revealed"
            },
            {
                "source": "CT,findings",
                "target": "three",
                "label": "revealed nodal FDG uptake in"
            },
            {
                "source": "data",
                "target": "non-human primates",
                "label": "obtained from"
            },
            {
                "source": "data",
                "target": "primates exposed to MERS",
                "label": "obtained from"
            },
            {
                "source": "data",
                "target": "non-human primates exposed to MERS",
                "label": "obtained from"
            },
            {
                "source": "data",
                "target": "non-human primates exposed",
                "label": "obtained from"
            },
            {
                "source": "data",
                "target": "primates exposed",
                "label": "obtained from"
            },
            {"source": "data", "target": "primates", "label": "obtained from"},
            {
                "source": "imaging,data",
                "target": "first time",
                "label": "evident indicate for"
            },
            {
                "source": "imaging,data",
                "target": "time",
                "label": "evident indicate for"
            },
            {
                "source": "imaging,data",
                "target": "first time",
                "label": "indicate for"
            },
            {"source": "imaging,data", "target": "time", "label": "indicate for"},
            {
                "source": "Multiple,peripheral",
                "target": "right lung",
                "label": "is in"
            },
            {
                "source": "Multiple,peripheral,GGOs",
                "target": "right lung",
                "label": "is in"
            },
            {"source": "fectious diseases", "target": "this", "label": "demonstrate"},
            {
                "source": "imaging,modality",
                "target": "diagnostic role",
                "label": "may play"
            },
            {
                "source": "imaging,modality",
                "target": "complementary diagnostic role",
                "label": "may play"
            },
            {
                "source": "imaging,modality",
                "target": "complementary role",
                "label": "may play"
            },
            {"source": "imaging,modality", "target": "role", "label": "may play"},
            {"source": "differences", "target": "sample", "label": "is in"},
            {"source": "caveats", "target": "first time", "label": "show for"},
            {"source": "caveats", "target": "time", "label": "show for"},
            {
                "source": "Compliance",
                "target": "ethical standards",
                "label": "is with"
            },
            {"source": "tive study", "target": "insti", "label": "was approved by"},
            {"source": "consent", "target": "waived", "label": "was"}
        ]
    }
