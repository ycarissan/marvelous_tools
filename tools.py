import argparse
from skspatial.objects import Plane
from skspatial.objects import Points
from geometry.geometry import Geometry

def main():
    parser = argparse.ArgumentParser(
        description='Great tools!',
        epilog="test"
        )
    parser.add_argument(
        'geomfile',
        type=str,
        help="Geometry file in xyz format. default: %(default)s",
        default="naphtalene.xyz")
    parser.add_argument(
        '--list_of_indices','-l',
        type=str,
        help="Comma separated list of indices (no space allowed): %(default)s",
        default="1,2,3")
    parser.add_argument(
        '--distance','-d',
        type=float,
        help="distance from the plane: %(default)s",
        default="1.0")
    parser.add_argument(
        '--phase','-p',
        type=int,
        help="phase (above +1 or below -1) : %(default)s",
        default="1")
    args = parser.parse_args()
    for arg in vars(args):
        print("{:} ... {:}".format(arg, getattr(args, arg)))

    geomfile = args.geomfile
    list_of_indices = [int(s.strip()) for s in args.list_of_indices.split(",")]
    distance = args.distance
    phase = args.phase
    distance = distance * phase

    geom = Geometry(geomfile)

    coords=[]
    for i in list_of_indices:
        coords.append(geom.getXYZ(i-1))
    points = Points(coords)
    
    plane = Plane.best_fit(points)
    vector = plane.normal*distance

    orig = points.centroid()
    target = orig + vector

    print("Target: {}".format(target))

if __name__=="__main__":
    main()

