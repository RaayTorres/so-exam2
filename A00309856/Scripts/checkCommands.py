from subprocess import Popen, PIPE

def cMemoria():
  vmstat_process = Popen(["vmstat", "-s","-S","m"], stdout=PIPE,stderr=PIPE)
  listado_stats= Popen(["awk", '{print $1}' ],stdin=vmstat_process.stdout, stdout=PIPE, stderr=PIPE).communicate()[0].split('\n')

  print(listado_stats)
  return filter(None, listado_stats)


def cCpu():
  mpstat_process = Popen(["mpstat"], stdout=PIPE, stderr=PIPE)
  awk_process = Popen(["awk", '{print $3}'], stdin=mpstat_process.stdout, stdout=PIPE, stderr=PIPE).communicate()[0].split('\n')

  return filter(None, awk_process)


def cDisco():
        df_process = Popen(["df","-h",'/dev/mapper/cl-root'], stdout=PIPE, stderr=PIPE)
        awk_process = Popen(["awk", '{print $4}'], stdin=df_process.stdout, stdout=PIPE, stderr=PIPE).communicate()[0].split('\n')


        return  filter(None, awk_process)

def eServicio():
        service_process = Popen(["/usr/sbin/service","sshd","status"], stdout=PIPE, stderr=PIPE)
        awk_process = Popen(["awk",'-F' ,'Active:', '{print $2}'], stdin=service_process.stdout, stdout=PIPE, stderr=PIPE).communicate()[0].split('\n')

        return filter(None, awk_process)
