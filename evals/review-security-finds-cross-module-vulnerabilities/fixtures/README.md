# archiver

Command-line tool that packs the clinic's scanned documents into archives and
restores the archives partner sites send back. Partner sites upload archives
over SFTP into `/srv/inbox`, choosing the file names. Staff run the CLI over
SSH under their own Unix account: `archiver restore /srv/inbox/<file>` unpacks
one archive into `/srv/documents`, and `archiver share <doc_id>` prints a
token the partner portal accepts, without any other login, to download that
document. Roles come from `/etc/archiver/roles` (`name: role` per line).
