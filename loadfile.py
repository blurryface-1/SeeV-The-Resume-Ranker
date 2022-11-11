import os
import textract as tx

# res_folder = "./Naive-Resume-Matching-master/Naive-Resume-Matching-master/Data/Resumes1/"
res_folder = "./Data/Resumes/"
res_txt = "./Data/res txt/"
job_folder = './Data/JobDesc/'
job_txt = "./Data/job txt/"



def docs_to_txt(c,doc):
    if doc=='Resume':
        if c=='a':
            for filename in os.listdir(res_folder):
                text = tx.process(res_folder+filename, encoding='ascii')
                text = str(text, 'utf-8')
                with open(res_txt+filename.split(".")[0]+".txt", 'w') as f:
                    f.write(text)
            return True
        elif c=='w':
            # delete all files in the directory
            for filename in os.listdir(res_txt):
                os.remove(res_txt+filename)
            
            for filename in os.listdir(res_folder):
                text = tx.process(res_folder+filename, encoding='ascii')
                text = str(text, 'utf-8')
                with open(res_txt+filename.split(".")[0]+".txt", 'w') as f:
                    f.write(text)
            return True
    
    elif doc=='Job':
        if c=='a':
            for filename in os.listdir(job_folder):
                text = tx.process(job_folder+filename, encoding='ascii')
                text = str(text, 'utf-8')
                with open(job_txt+filename.split(".")[0]+".txt", 'w') as f:
                    f.write(text)
            return True
        elif c=='w':
            # delete all files in the directory
            for filename in os.listdir(job_txt):
                os.remove(job_txt+filename)
            for filename in os.listdir(job_folder):
                text = tx.process(job_folder+filename, encoding='ascii')
                text = str(text, 'utf-8')
                with open(job_txt+filename.split(".")[0]+".txt", 'w') as f:
                    f.write(text)
            return True

def get_jobfiles():
    list = os.listdir(job_folder)
    for i in range(len(list)):
        list[i]=list[i].split(".")[0]
    return list


def load_job(title):
    text = tx.process(job_folder+title+".docx", encoding='ascii')
    text = str(text, 'utf-8')
    return text

def save_file(data, path):
    with open(path+data.filename, 'wb') as f:
        f.write(data.read())

def load_job_txt(filename):
    with open(job_txt+filename+".txt", 'r') as f:
        text = f.read()
    return text
