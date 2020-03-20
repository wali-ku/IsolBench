import sys, re
import matplotlib.pyplot as plt

def parse (filename):
    bw = []
    rex = r'^.* bw = ([\d.]+) mbps.*$'
    with open (filename, 'r') as fdi:
        lines = fdi.readlines ()

    for line in lines:
        m = re.match (rex, line)

        if m:
            bw.append (float (m.group (1)))

    return bw [:-1]

def plot (data):
    xAxis = range (0, len (data))
    plt.bar (xAxis, data, width = 0.6, color = 'red', edgecolor = 'k', lw = 0.75, ls = '--', align = 'edge')
    plt.ylabel ("Bandwidth (MB/s)", fontweight = 'bold', fontsize = 'x-large')
    plt.xlabel ("Time (sec)", fontweight = 'bold', fontsize = 'x-large')
    plt.title ("Ratio Based MemGuard Throttling", fontweight = 'bold', fontsize = 'xx-large')
    plt.grid (axis = 'y', color = 'grey', ls = '--')
    plt.savefig ('gpu_map.pdf', bbox_inches = 'tight')

    return


def main ():
    filename = sys.argv [1]

    bw = parse (filename)
    plot (bw)

    return

if __name__ == '__main__':
    main ()

